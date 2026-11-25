# file_organizer.py
import os
import shutil

# 1. किस तरह की फाइल को किस फ़ोल्डर में भेजना है (Dictionary)
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"]
}

# 2. जिस फ़ोल्डर को साफ़ करना है (अभी हम टेस्ट फ़ोल्डर साफ़ करेंगे)
TARGET_FOLDER = r"C:\Users\Sikandar Bharti\Downloads\messy_folder"


def setup_demo_files():
    """यह फंक्शन टेस्ट करने के लिए कुछ नकली (Dummy) फाइल्स बनाएगा"""
    os.makedirs(TARGET_FOLDER, exist_ok=True)
    demo_files = [
        "pic1.jpg", "bill.pdf", "song.mp3",
        "notes.txt", "family.png", "movie.mp4"
    ]
    for file in demo_files:
        path = os.path.join(TARGET_FOLDER, file)
        with open(path, "w") as f:
            f.write("Demo content")
    print(f"📦 'messy_folder' me 6 alag-alag files bana di gayi hain!\n")


def organize_folder():
    """यह मुख्य ऑटोमेशन इंजन है जो फाइलों को छांटेगा"""
    print("⏳ Scanning folder aur files ko organize kiya ja raha hai...")

    # फ़ोल्डर के अंदर की सारी फाइलों की लिस्ट निकालना
    files = os.listdir(TARGET_FOLDER)

    for file in files:
        file_path = os.path.join(TARGET_FOLDER, file)

        # अगर यह खुद एक फ़ोल्डर है, तो इसे छोड़ दो
        if os.path.isdir(file_path):
            continue

        # फाइल का एक्सटेंशन निकालना (जैसे .jpg या .pdf)
        _, file_extension = os.path.splitext(file)
        file_extension = file_extension.lower()

        # चेक करना कि यह किस कैटेगरी में आता है
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                # उस कैटेगरी का फ़ोल्डर बनाएं (अगर पहले से नहीं है)
                category_folder = os.path.join(TARGET_FOLDER, category)
                os.makedirs(category_folder, exist_ok=True)

                # फाइल को नए फ़ोल्डर में खिसकाएं (Move)
                destination = os.path.join(category_folder, file)
                shutil.move(file_path, destination)
                print(f"🚚 Moved: {file} ➔ {category}/")
                moved = True
                break

        # अगर कोई अनजान फाइल है (जैसे .xyz), तो उसे Others में डाल दो
        if not moved:
            others_folder = os.path.join(TARGET_FOLDER, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, file))
            print(f"🚚 Moved: {file} ➔ Others/")

    print("\n🎉 Mubarak! Pura folder 1 second me saaf ho gaya!")


# 🚀 ऑटोमेशन शुरू करें:
#setup_demo_files()   # पहले 6 नकली फाइलें बनाईं
organize_folder()    # फिर 1 सेकंड में सबको छांट दिया!