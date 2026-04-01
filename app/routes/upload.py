import uuid, shutil, os
from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()
ALLOWED = {"image/jpeg", "image/png", "image/webp", "image/gif"}

@router.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED:
        raise HTTPException(400, "Only JPEG, PNG, WebP and GIF images are supported.")
    ext = file.filename.rsplit(".", 1)[-1] if "." in file.filename else "jpg"
    image_id = str(uuid.uuid4())
    dest = f"/tmp/{image_id}_original.{ext}"
    with open(dest, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"image_id": image_id, "filename": file.filename, "status": "uploaded"}
