# my_ai.py
from google import genai

# 🔑 1. अपनी कॉपी की हुई API Key यहाँ कोट्स के अंदर पेस्ट करें
API_KEY = "AIzaSyC_K67cTyhzmlUhKa9Tm9Mt_eGggGaiVpY"

# 🤖 2. Gemini क्लाइंट चालू करें
client = genai.Client(api_key=API_KEY)

print("🤖 AI Chatbot taiyar hai! Apna sawal puchiye:")
user_question = input("Aap: ")

print("\n⏳ Gemini soch raha hai...")

# 🚀 3. सवाल को Gemini AI मॉडल के पास भेजना
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_question
)

# 💬 4. AI का जवाब स्क्रीन पर दिखाना
print("\n🤖 Gemini ka Jawab:")
print(response.text)