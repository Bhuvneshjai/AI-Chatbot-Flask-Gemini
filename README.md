==============================
🤖 AI Chat System with Gemini
==============================

🔍 Overview:
-------------
A lightweight, intelligent chatbot built using FastAPI and Google's Gemini API. Type your query, and the bot responds like a genius — smooth, fast, and surprisingly smart!

🎯 What It Does:
------------------
- Collects user input via a simple web form 📝
- Sends it to Gemini (Google’s Generative AI) 💡
- Returns human-like responses directly to the UI 💬

⚙️ Tech Stack:
---------------
- FastAPI
- Google Gemini API (`google-generativeai`)
- Uvicorn
- Jinja2 Templates
- Python-dotenv

🚀 Setup Instructions:
------------------------
1️⃣ Install required libraries:
    ```bash
    pip install fastapi uvicorn google-generativeai python-dotenv jinja2
    ```

2️⃣ Create a `.env` file in the root directory and add your API key:
    ```
    GEMINI_API_KEY=your_google_gemini_api_key_here
    ```

3️⃣ Start the FastAPI server:
    ```bash
    uvicorn main:app --reload --port 8000
    ```

4️⃣ Visit in your browser:
    ```
    http://127.0.0.1:8000
    ```

🙅‍♂️ Git Ignore Tips:
-----------------------
To avoid pushing sensitive files to GitHub, add these lines to your `.gitignore`:
```
.env 
pycache/
*.pyc
venv/
```


✅ Sample Prompt:
-------------------
User: *"Give me a productivity hack."*  
Gemini: *"Use the Pomodoro technique — 25 minutes work, 5 minutes rest. Works like a charm!"*

💡 Use Cases:
--------------
- Virtual assistant
- FAQ bot
- Productivity tool
- Code explanation bot
- Creative idea generator

💬 Final Thought:
-------------------
🧠 *“Turning text into brilliance — one Gemini call at a time.”*
