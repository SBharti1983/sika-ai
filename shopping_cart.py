def run_cart():
    # 4 स्पेस अंदर: पूरा कोड यहाँ होना चाहिए
    cart = []
    print("--- Grocery Store me Swagat hai! ---")

    while True:
        # 8 स्पेस अंदर
        item = input("Saaman ka naam: ")
        if item == "done":
            break
        cart.append(item)

    for saaman in cart:
        print(f"- {saaman}")
    # 🛑 यहाँ पर पूरा फंक्शन खत्म!


# --------------------------------------------------
# 👇 अगर आपको फंक्शन के बाद बाहर कुछ लिखना हो, तो ऐसे लिखें:
print("Ye line function ke BAAD/BAHAR hai!")