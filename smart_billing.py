from discount_calculator import calculate_final_price

# 1. दुकान की रेट लिस्ट (Dictionary)
menu = {
        "milk": 60,
        "bread": 40,
        "egg": 10,
        "coffee": 150
      }
cart = []
total_bill = 0
print("\n--- 🛒 Kirana Store Rate List ---")
for item, rate in menu.items():
    print(f"{item.capitalize()} : ₹{rate}")
print("---------------------------------")
print("(Kharidari khatam karne ke liye 'done' likhein)\n")
# 2. यूजर से खरीदारी करवाना
while True:
    choice = input("Kya khareedna chahte hain? : ").lower()
    if choice == "done":
        break
    elif choice in menu:
        cart.append(choice)
        total_bill = total_bill + menu[choice]  # भाव जोड़ना
        print(f"'{choice}' jud gaya! (₹{menu[choice]})")
    else:
        print("❌ Maaf kijiye, ye saaman uplabdh nahi hai!")
# 3. फाइनल बिल प्रिंट करना
print("\n=========================")
print("       FINAL BILL        ")
print("=========================")
for item in cart:
    print(f"- {item} : ₹{menu[item]}")
print("-------------------------")

discount= calculate_final_price(total_bill)

print(f"Total Discount on the bill: ₹{discount}")
print(f"Kul Rashi (Total): ₹{total_bill-discount}")
print("=========================\n")
