from PIL import Image
import numpy as np

TEMPLATES = {
    "beach":   "https://res.cloudinary.com/demo/video/upload/v1/samples/ocean.mp4",
    "nature":  "https://res.cloudinary.com/demo/video/upload/v1/samples/elephants.mp4",
    "city":    "https://res.cloudinary.com/demo/video/upload/v1/samples/sea-turtle.mp4",
    "sunset":  "https://res.cloudinary.com/demo/video/upload/v1/samples/ocean.mp4",
    "snow":    "https://res.cloudinary.com/demo/video/upload/v1/samples/elephants.mp4",
    "indoor":  "https://res.cloudinary.com/demo/video/upload/v1/samples/sea-turtle.mp4",
    "default": "https://res.cloudinary.com/demo/video/upload/v1/samples/ocean.mp4",
}

def classify_scene(image_path: str) -> str:
    try:
        img = Image.open(image_path).convert("RGB").resize((100, 100))
        arr = np.array(img, dtype=float)
        r, g, b = arr[:,:,0].mean(), arr[:,:,1].mean(), arr[:,:,2].mean()
        brightness = (r + g + b) / 3

        if brightness > 220:
            return "snow"
        if b > r + 20 and b > g and brightness > 120:
            return "beach"
        if g > r + 15 and g > b:
            return "nature"
        if r > 160 and g > 100 and b < 100:
            return "sunset"
        if r < 100 and g < 100 and b < 120 and brightness < 80:
            return "city"
        return "indoor"
    except Exception:
        return "default"

def get_video_template(scene_type: str) -> str:
    return TEMPLATES.get(scene_type, TEMPLATES["default"])
