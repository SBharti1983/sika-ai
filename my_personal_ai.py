# my_personal_ai.py
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
# 🔐 1. पहले लोड किया
load_dotenv()
# 🔑 2. अब Key निकाली
API_KEY = os.getenv("GEMINI_API_KEY")
# 🤖 3. Client चालू किया
client = genai.Client(
    api_key=API_KEY,
    http_options={"api_version": "v1beta"}
)

SYSTEM_PROMPT = "Aap ek friendly aur helpful Python Coding Tutor hain. Har cheez saral Hindi/Hinglish me samjhaiye."

print("===========================================")
print("🤖 MERA AI CHATBOT (Google Gemini Powered)")
print("   (Chat band karne ke liye 'exit' likhein)")
print("===========================================\n")

while True:
    user_question = input("\n👤 Aap: ")

    if user_question.lower() in ["exit", "quit", "bye"]:
        print("🤖 Gemini: Alvida! Phir milte hain. 👋")
        break

    if not user_question.strip():
        continue

    print("⏳ Soch raha hai...")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_question,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )
    )

    print(f"\n🤖 Gemini: {response.text}")