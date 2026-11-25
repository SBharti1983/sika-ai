import os
from datetime import datetime

filename = "receipt.txt"

billing_name = input("Apna naam batayein: ")
billing_amount = float(input("Apni bill ampunt batayein: "))
now = datetime.now().date()

if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("Namaste! Welcome to Qshop.\n\n")

with open(filename, "a") as file:
            file.write("=============================\n")
            file.write(f"Grahak ka Naam : {billing_name}\n")
            file.write(f"Kul Rashi : {billing_amount}\n")
            file.write(f"Date : {now}\n")
            file.write("Dhanyawad! Phir aaiyega!\n")
            file.write("=============================")

with open(filename, "r") as file:
              content = file.read()
              print(content)

