# 🎬 Video Summary Generator

A simple Python desktop application that generates concise summaries from video files. The app uses **Google Gemini** for transcription and summarization, with a user-friendly interface built using **Tkinter**.

---

## 🚀 Features

- 📹 Upload and process video files  
- 🧠 Automatic transcription using Google Gemini  
- ✂️ Generate short, readable summaries  
- 🖥️ Simple GUI powered by Tkinter  
- ⚡ Easy one-click execution via `run.bat`  

---

## 🛠️ Tech Stack

- **Python**
- **Tkinter** (GUI)
- **Google Gemini API** (transcription & summarization)
- **python-dotenv** (environment variable management)

---

## 📂 Project Structure
video-summary-generator/
│
├── app.py # Main application file
├── run.bat # Script to launch the app
├── .env # API key configuration
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/video-summary-generator.git](https://github.com/DoctorNULL/VideoSummaryGenerator)
cd video-summary-generator
```

### 2. Install Dependencies

Make sure you have Python installed (3.8+ recommended), then run:
```
pip install -r requirements.txt
```
### 3. Configure Environment Variables

Create a .env file in the root directory and add your Google API key:
```
GOOGLE_API_KEY="Your API key"
```
⚠️ Keep this file private and do not share it publicly.

### 4. Run the Application

You can start the app in two ways:

Option A: Using the batch file (Windows)
run.bat
Option B: Directly with Python
python app.py

## 🧑‍💻 Usage
Launch the application
Upload a video file
Wait for transcription to complete
View the generated summary

## 🔐 Environment Variables
```
GOOGLE_API_KEY	Your Google Gemini API key
```

## 📝 Notes
Ensure your API key has access to Google Gemini services
Large video files may take longer to process
Internet connection is required for API calls

## 📌 Future Improvements
Export summaries to text/PDF
Add progress indicators
Drag-and-drop video upload

🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request.

📄 License
This project is licensed under the MIT License.
