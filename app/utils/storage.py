import cloudinary
import cloudinary.uploader
import os

def upload_video(file_path: str) -> str:
    cloudinary.config(cloudinary_url=os.environ.get("CLOUDINARY_URL"))
    result = cloudinary.uploader.upload(
        file_path,
        resource_type="video",
        folder="timeecho",
    )
    return result["secure_url"]
