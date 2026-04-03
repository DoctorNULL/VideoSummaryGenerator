import os
from tkinter.messagebox import showerror, showinfo
from google import genai
from dotenv import load_dotenv

load_dotenv()

def generate_md_file(file_name: str = "GeneratedMarkdown"):

    if  not os.getenv("GOOGLE_API_KEY"):
        showerror("AI Error", "Can't find google api key, please provide it in environment")
        return

    if not os.path.isfile("extracted.mp3"):
        showerror("AI Error", "Can't find audio file, Please make sure it is named extracted.mp3")
        return

    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    audio = client.files.upload(file="extracted.mp3")

    response = client.models.generate_content_stream(
        model="gemini-3-flash-preview",
        config=genai.types.GenerateContentConfig(
            system_instruction="You are a professor who summarize lectures focusing on the most important details and notes. "
                               "Given the user transcript of a lecture generate a markdown content that summarize this lecture. "
                               "Preserve all relative information to the topic, Mention all session main topic, tools, topics and summaries mentioned and "
                               "Ignore all un relevant talks to the main topic of the session."
        ),
        contents=["Explain this audio and find all information inside it", audio]
    )

    res = ""

    for chunk in response:
        print(chunk.text, end="")
        res += chunk.text

    with open(f"{file_name}.md", 'w') as file:
        file.write(res)

    showinfo("Complete", f"Video transcript extracted successfully in {file_name}.md")