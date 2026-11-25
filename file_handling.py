# file_handling.py

# ✍️ 1. फ़ाइल में लिखना ('w' = Write Mode)
with open("mera_note.txt", "w") as file:
    file.write("Namaste! Ye meri pehli Python dwara banayi gayi file hai.\n")
    file.write("Python seekhna sach me bahut mazedaar hai!\n")

print("✅ File safaltapoorvak ban gayi aur save ho gayi!")

# 📖 2. फ़ाइल को पढ़ना ('r' = Read Mode)
with open("mera_note.txt", "r") as file:
    content = file.read()

print("\n--- File ka Content ---")
print(content)