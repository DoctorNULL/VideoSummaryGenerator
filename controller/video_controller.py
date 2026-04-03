from moviepy import VideoFileClip

def extract_audio(video_path: str):
    video = VideoFileClip(video_path.strip())
    audio = video.audio
    audio.write_audiofile("extracted.mp3")
    audio.close()
    video.close()