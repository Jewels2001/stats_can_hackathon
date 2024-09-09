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
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)