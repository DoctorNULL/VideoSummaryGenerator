import tkinter as tk
from controllers import ai_controller, ui_controller, video_controller
from os.path import splitext, basename

def convert():
    video_controller.extract_audio(text.get("1.0", "end"))
    try:
        ai_controller.generate_md_file(file_name=splitext(basename(text.get("1.0", "end")))[0])
    except:
        ai_controller.generate_md_file()

app = tk.Tk()
app.title("Video Summarizer App")
app.geometry("500x300")

text = tk.Text(app, height=5, width=40)
text.pack(pady=10)

picker = tk.Button(app, text="Pick", command=lambda : ui_controller.pick_video(text))
picker.pack(pady=5)

btn = tk.Button(app, text="Convert", command= convert)
btn.pack(pady=5)

app.mainloop()