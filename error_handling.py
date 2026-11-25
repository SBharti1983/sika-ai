# error_handling.py

# while True:
#     try:
#         # 1. यहाँ हम नंबर में बदलने की कोशिश करेंगे
#         age = int(input("Apni umar (number me) batayein: "))
#
#         # अगर ऊपर की लाइन बिना एरर के चल गई, तो यह चलेगा:
#         print(f"✅ Bahut badhiya! Aapki age {age} saal hai.")
#         break  # सही इनपुट मिला, लूप बंद!
#
#     except ValueError:
#         # 2. अगर यूजर ने 'abc' या कुछ गलत लिखा, तो कोड क्रैश होने के बजाय यहाँ आएगा:
#         print("❌ Are bhai! Kripya sirf NUMBER likhein (jaise 25), shabd nahi!\n")

while True:
    try:
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))

        result = num1 / num2
        print(f"Result: {result}")
        break

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")
