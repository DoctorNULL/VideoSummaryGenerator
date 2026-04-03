from faster_whisper import WhisperModel

def extract_transcript():
    model = WhisperModel("Whisper", local_files_only=True, download_root="./", compute_type="float16")

    segments, info = model.transcribe("extracted.mp3", "ar", multilingual=True, beam_size=5)

    with open("transcript.txt", "w", encoding="utf-8") as file:
        for seg in segments:
            print(seg.text)
            file.write(seg.text + " ")