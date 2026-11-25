# my_first_ai_agent.py
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=API_KEY,
    http_options={"api_version": "v1beta"}
)

# 🛠️ TOOL 1: यह फंक्शन AI का हाथ बनेगा (फाइल बनाने के लिए)
def save_note_to_file(filename: str, content: str) -> str:
    """Saves a note or text message into a file on the computer.
    Args:
        filename: Name of the file, e.g. reminder.txt or meeting.txt
        content: The text content to write inside the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    return f"Success: File '{filename}' has been created and saved on computer."


print("===========================================")
print("🤖 MERA PEHLA AUTONOMOUS AI AGENT 🛠️")
print("   (Ask me to chat OR order me to make files!)")
print("===========================================\n")

# 🧠 AI को अपना टूल सौंपना:
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        tools=[save_note_to_file]  # 👈 यहाँ हमने AI को अपना टूल दे दिया!
    )
)

while True:
    user_question = input("\n👤 Aap: ")

    if user_question.lower() in ["exit", "quit", "bye"]:
        print("🤖 Agent: Alvida! Kaam ho gaya. 👋")
        break

    if not user_question.strip():
        continue

    print("⏳ Agent soch raha hai aur action le raha hai...")

    # AI अपने आप समझ जाएगा कि कब बात करनी है और कब फाइल बनानी है
    response = chat.send_message(user_question)

    print(f"\n🤖 Agent: {response.text}")