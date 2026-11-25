# oop_bank.py
class BankAccount:
    bank_name = "State Bank of India"
    branch_city = "Delhi"
    # 🏗️ __init__ (कंस्ट्रक्टर): जब भी नया खाता खुलेगा, यह अपने आप चलेगा
    def __init__(self, name, balance):
        self.holder_name = name      # ग्राहक का नाम
        self.account_balance = balance  # शुरुआती बैलेंस

    # 💰 पैसे जमा करने का फंक्शन (Method)
    def deposit(self, amount):
        self.account_balance += amount
        print(f"₹{amount} jama hue. Naya Balance: ₹{self.account_balance}")

    # 🏧 पैसे निकालने का फंक्शन (Method)
    def withdraw(self, amount):
        if amount > self.account_balance:
            print("❌ Insufficient balance! Paise nahi nikale ja sakte.")
        else:
            self.account_balance -= amount
            print(f"₹{amount} nikale gaye. Bacha Balance: ₹{self.account_balance}")

    # 📋 बैलेंस चेक करने का फंक्शन
    def show_info(self):
        print(f"\nKhata: {self.holder_name} | Kul Balance: ₹{self.account_balance}\n")

# सिकंदर का खाता खोला (₹5000 के साथ)
sikandar_account = BankAccount("Sikandar", 5000)
rahul_account = BankAccount("Rahul", 1000)

# सिकंदर के खाते में काम करते हैं:
print(BankAccount.bank_name)
sikandar_account.show_info()
sikandar_account.deposit(2000)    # 2000 जमा किए
sikandar_account.withdraw(1500)   # 1500 निकाले

# राहुल का खाता देखते हैं (उसका खाता बिल्कुल अलग रहेगा!)
rahul_account.show_info()