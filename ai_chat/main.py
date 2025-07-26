import os
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

# Initialize FastAPI app
app = FastAPI()

# Home route
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>Welcome</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f5f5f5;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    text-align: center;
                    background: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 0 20px rgba(0,0,0,0.1);
                }
                a.button {
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    font-size: 16px;
                    color: white;
                    background-color: #007bff;
                    border: none;
                    border-radius: 5px;
                    text-decoration: none;
                }
                a.button:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>👋 Welcome to the AI Chat API</h2>
                <p>Use the button below to chat with Gemini!</p>
                <a class="button" href="/chat">Start Chat</a>
                <p style="margin-top: 20px;"><a href="/docs">🔍 Swagger Docs</a></p>
            </div>
        </body>
    </html>
    """

# Chat form route
@app.get("/chat", response_class=HTMLResponse)
async def chat_form():
    return """
    <html>
        <head>
            <title>Gemini Chat</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #eef;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .chat-container {
                    background: #fff;
                    padding: 30px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    text-align: center;
                }
                input[type='text'] {
                    padding: 10px;
                    width: 300px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                button {
                    padding: 10px 20px;
                    margin-left: 10px;
                    background-color: #28a745;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #218838;
                }
            </style>
        </head>
        <body>
            <div class="chat-container">
                <h2>💬 Talk to Gemini</h2>
                <form action="/chat" method="post">
                    <input type="text" name="user_input" placeholder="Ask me anything..." required />
                    <button type="submit">Send</button>
                </form>
                <p style="margin-top: 20px;"><a href="/">🏠 Back Home</a></p>
            </div>
        </body>
    </html>
    """

# Chat response route
@app.post("/chat", response_class=HTMLResponse)
async def chat_response(user_input: str = Form(...)):
    try:
        response = model.generate_content(user_input)
        answer = response.text
    except Exception as e:
        answer = f"❌ Error: {str(e)}"

    return """
    <html>
        <head>
            <title>Gemini Response</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #fdfdfd;
                    padding: 40px;
                }}
                .box {{
                    background: #f0f8ff;
                    padding: 20px;
                    border-radius: 10px;
                    border: 1px solid #ccc;
                }}
                strong {{
                    display: block;
                    margin-bottom: 5px;
                }}
                .answer {{
                    margin-top: 10px;
                    font-style: italic;
                    color: #333;
                    white-space: pre-line;
                }}
                a {{
                    margin-top: 20px;
                    display: inline-block;
                    text-decoration: none;
                    color: #007bff;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
            </style>
        </head>
        <body>
            <h2>🤖 Gemini's Reply</h2>
            <div class="box">
                <p><strong>You asked:</strong> {user_input}</p>
                <p class="answer"><strong>Gemini says:</strong><br>{answer}</p>
            </div>
            <br><a href="/chat">↩️ Ask Another</a>
        </body>
    </html>
    """.format(user_input=user_input, answer=answer)


# Optional: List available models and their capabilities
if __name__ == "__main__":
    for m in genai.list_models():
        print(m.name, m.supported_generation_methods)