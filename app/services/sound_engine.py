SOUNDS = {
    "beach":   "https://cdn.pixabay.com/audio/2022/03/10/audio_270f57e391.mp3",
    "nature":  "https://cdn.pixabay.com/audio/2022/05/16/audio_1ef1c22ad2.mp3",
    "city":    "https://cdn.pixabay.com/audio/2021/09/06/audio_6f3b96c4aa.mp3",
    "sunset":  "https://cdn.pixabay.com/audio/2022/03/10/audio_270f57e391.mp3",
    "snow":    "https://cdn.pixabay.com/audio/2022/01/18/audio_d0a3c6c7c9.mp3",
    "indoor":  "https://cdn.pixabay.com/audio/2022/01/18/audio_d0a3c6c7c9.mp3",
    "default": "https://cdn.pixabay.com/audio/2022/03/10/audio_270f57e391.mp3",
}

def get_sound_url(scene_type: str) -> str:
    return SOUNDS.get(scene_type, SOUNDS["default"])
