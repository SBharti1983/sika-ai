# live_api.py
import requests

print("⏳ Internet se live data mangaya ja raha hai...")

# 🌐 इंटरनेट पर एक फ्री API से एक मजेदार तथ्य (Fact) मंगाना
url = "https://uselessfacts.jsph.pl/api/v2/facts/random"

response = requests.get(url)

# API से आया जवाब (JSON रूप में)
data = response.json()

print("\n--- 💡 Aaj ka Rochak Tathya (Live Fact) ---")
print(data["text"])
print("------------------------------------------\n")