from tkinter import filedialog, Text

def pick_video(path: Text):
    file_path = filedialog.askopenfilename(
        title="Select video",
        filetypes=[
            ("Video files", "*.mp4 *.avi *.mov *.mkv"),
            ("All files", "*.*")
        ]
    )

    if file_path:
        path.delete("1.0", "end")
        path.insert("1.0", file_path)