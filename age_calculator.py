# Day 1: शुरुआत करते हैं (Variables & User Input)
# 1. यूजर से इनपुट लेना
# name = input("Apna naam batayein: ")
# age = input("Apni umar (age) batayein: ")
# city = input("Apni City Bataye: ")
# programming_language = input("Apni Programming Language Bataye: ")

# 2. स्क्रीन पर आउटपुट दिखाना
# print(f"Namaste {name}! Aapki age {age} saal hai.")
# print(f"Aur Aapki Programming Language {programming_language} hai.")
# print(f"Aapki City {city} hai.")
# ----------------------------------------
# Data Types और Type Conversion (str vs int)

# age = input("Apni umar batayein:")
# print(age + 5)  # ❌ यहाँ ERROR आ जाएगा!
# int() लगाने से टेक्स्ट असली नंबर बन जाता है
from datetime import datetime
now = datetime.now().year
# 🔄 यह लूप तब तक यूजर से पूछता रहेगा जब तक वो सही साल न डाल दे
while True:
    birth_year = int(input(f"Apni Birth Year batayein (1900 se {now} ke beech): "))
    # जाँच: क्या साल 1900 और चालू साल के बीच में है?
    if 1900 <= birth_year <= now:
        break  # ✅ सही इनपुट मिला! लूप तोड़कर बाहर आ जाओ
    else:
        print(f"❌ Galat saal! Kripya sahi 4-digit saal daalein.\n")
# 🎯 लूप से बाहर आने के बाद उम्र की कैलकुलेशन

calculated_age =  now - birth_year
print(f"Aap lagbhag {calculated_age} saal ke hain!")

# 🚦 यहाँ से शुरू होती हैं शर्तें (Conditions):
if calculated_age >= 60:
    print("Aap Senior Citizen hain. 🧓")
elif calculated_age >= 18:
    print("Aap Adult hain, vote aur drive kar sakte hain! 🚗")
else:
    print("Aap abhi minor hain, chill kijiye aur coding seekhiye! 🎮")
#A while loop in Python repeatedly executes a block of code as long as a specified condition evaluates to True
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Skips printing 3
    if i == 5:
        break     # Exits loop early; prevents the 'else' block from running
    print(i)
else:
    print("Loop finished normally")

while True:
    password = input("Enter the secret password: ")
    if password == "python123":
        print("Access granted!")
        break
    else:
        print(f"❌ Password is wrong.\n")