"""
This module queries Google's Gemini LLM
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai


# Retrieve the env variables - contains API key!
load_dotenv()
API_KEY = os.environ["JULIE_GEMINI_API_KEY"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "How much does it cost to make this recipe?"},
        {"role": "model", "parts": "I can figure that out for you! What recipe would you like to make?"}
    ]
)
response = chat.send_message("I want to make spaghetti bolognese")
print(response.text)
response = chat.send_message("What food did I want to make?")
print(response.text)