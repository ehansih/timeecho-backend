import uuid, os, httpx, asyncio
from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from app.services.ai_engine import classify_scene, get_video_template
from app.services.sound_engine import get_sound_url
from app.utils.ffmpeg_util import merge_video_audio
from app.utils.storage import upload_video

router = APIRouter()

# In-memory job store (MVP)
jobs: dict = {}

class GenerateRequest(BaseModel):
    image_id: str

async def download_file(url: str, dest: str):
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.get(url)
        r.raise_for_status()
        with open(dest, "wb") as f:
            f.write(r.content)

async def process_job(job_id: str, image_id: str, image_path: str):
    try:
        jobs[job_id]["status"] = "processing"

        # Step 1: classify scene
        scene = classify_scene(image_path)
        jobs[job_id]["scene"] = scene

        # Step 2: get template URLs
        video_url = get_video_template(scene)
        audio_url = get_sound_url(scene)

        # Step 3: download template video + audio
        video_tmp = f"/tmp/{job_id}_video.mp4"
        audio_tmp = f"/tmp/{job_id}_audio.mp3"
        output_tmp = f"/tmp/{job_id}_output.mp4"

        await download_file(video_url, video_tmp)
        await download_file(audio_url, audio_tmp)

        # Step 4: merge with FFmpeg
        merge_video_audio(video_tmp, audio_tmp, output_tmp, duration=5)

        # Step 5: upload to Cloudinary
        final_url = upload_video(output_tmp)

        # Cleanup
        for f in [video_tmp, audio_tmp, output_tmp, image_path]:
            try: os.remove(f)
            except: pass

        jobs[job_id].update({"status": "done", "video_url": final_url})

    except Exception as e:
        jobs[job_id].update({"status": "error", "error": str(e)})

@router.post("/generate-video")
async def generate_video(req: GenerateRequest, background_tasks: BackgroundTasks):
    # Find image file
    matches = [f for f in os.listdir("/tmp") if f.startswith(req.image_id)]
    if not matches:
        raise HTTPException(404, "Image not found. Upload first.")
    image_path = f"/tmp/{matches[0]}"

    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "queued", "image_id": req.image_id}
    background_tasks.add_task(process_job, job_id, req.image_id, image_path)

    return {"job_id": job_id, "status": "queued"}

@router.get("/get-result/{job_id}")
def get_result(job_id: str):
    job = jobs.get(job_id)
    if not job:
        raise HTTPException(404, "Job not found.")
    return job
