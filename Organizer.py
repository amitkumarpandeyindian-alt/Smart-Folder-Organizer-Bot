import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

# Har prakar ki files ke liye complete list
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp", ".ico"],
    "Documents_And_Notes": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv"],
    "Coding_Files": [".cpp", ".c", ".py", ".java", ".html", ".css", ".js", ".json", ".sql"],
    "Softwares_And_Zips": [".exe", ".msi", ".zip", ".rar", ".7z", ".iso"],
    "Audio_Video": [".mp4", ".mkv", ".avi", ".mp3", ".wav", ".flac"],
    "Presentations": [".pptx", ".ppt"]
}

def get_category(extension):
    ext = extension.lower()
    for category, extensions_list in FILE_CATEGORIES.items():
        if ext in extensions_list:
            return category
    return "Other_Files"

def make_unique_path(dest_folder, filename):
    """Agar same naam ki file pehle se ho toh overwrite nahi karega"""
    name, ext = os.path.splitext(filename)
    counter = 1
    new_path = os.path.join(dest_folder, filename)
    while os.path.exists(new_path):
        new_path = os.path.join(dest_folder, f"{name}_{counter}{ext}")
        counter += 1
    return new_path

def organize_selected_folder():
    # Folder select karne ka pop-up box kholna
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    
    print("Pop-up window mein wo folder select kar jisko organize karna hai...")
    target_folder = filedialog.askdirectory(title="Select Folder to Organize")

    if not target_folder:
        print("❌ Tune koi folder select nahi kiya!")
        return

    print("\n==================================================")
    print(f"SCANNING FULL FOLDER: {target_folder}")
    print("==================================================\n")

    files = os.listdir(target_folder)
    moved_count = 0
    this_script = os.path.basename(__file__)

    for item in files:
        item_path = os.path.join(target_folder, item)

        # Folders ko aur khud ki script ko skip karo
        if os.path.isdir(item_path) or item == this_script:
            continue

        _, extension = os.path.splitext(item)
        if not extension:
            continue

        category_name = get_category(extension)
        category_folder = os.path.join(target_folder, category_name)
        os.makedirs(category_folder, exist_ok=True)

        final_dest = make_unique_path(category_folder, item)
        
        try:
            shutil.move(item_path, final_dest)
            print(f"Moved: {item[:25]:25} ---> {category_name}/")
            moved_count += 1
        except Exception as e:
            print(f"Skipped {item} (File khuli hui hai): {e}")

    print("\n==================================================")
    print(f"COMPLETE! Total {moved_count} files organize ho gayin!")
    print("==================================================")

if __name__ == "__main__":
    organize_selected_folder()
