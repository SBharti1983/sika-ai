# यह फंक्शन इनपुट में 'bill' लेगा
def calculate_final_price(bill):
    if bill >= 200:
        discount = bill * 0.10  # 10% की छूट
        final_amount = bill - discount
        # print(f"🎉 Mubarak! Aapko ₹{discount} ka discount mila!")
        return final_amount  # नया बिल वापस भेजा
    else:
        print("Discount paane ke liye kam se kam ₹200 ki kharidari karein.")
        return bill  # बिना डिस्काउंट के बिल वापस भेजा

# फंक्शन को इस्तेमाल करना:
my_bill = 250
paid_amount = calculate_final_price(my_bill)

print(f"Aapko sirf ₹{paid_amount} dene hain.")