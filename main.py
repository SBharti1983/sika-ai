# main.py
# import age_calculator
# import shopping_cart

# while True:
#     print("================================")
#     print("     MERA PYTHON DASHBOARD      ")
#     print("================================")
#     print("1. Age Calculator chalayein")
#     print("2. Shopping Cart chalayein")
#     print("3. Program band karein (Exit)")
#
#     choice = input("Apna vikalp chunein (1/2/3): ")
#     if choice == "1":
#         #calculator.run_calculator()  # calculator.py ka code chalega
#     elif choice == "2":
#         # shopping_cart.run_cart()  # shopping_cart.py ka code chalega
#     elif choice == "3":
#         print("Alvida! Program band ho raha hai. 👋")
#         break
#     else:
#         print("❌ Galat vikalp! Sirf 1, 2 ya 3 dabayein.\n")


def main():
    total = 0
    print("Enter numbers to add them up (type '0' to quit):")

    while True:
        user_input = input("> ")

        if not user_input.isdigit():
            print("Please enter a valid positive number.")
            continue

        number = int(user_input)

        if number == 0:
            break

        total += number

    print(f"Final total: {total}")


if __name__ == "__main__":
    main()