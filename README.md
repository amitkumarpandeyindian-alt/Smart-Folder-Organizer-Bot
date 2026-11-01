# Smart-Folder-Organizer-Bot

A simple Python script I built to clean up my cluttered Downloads and Desktop folders. It uses a Tkinter pop-up to pick any folder and automatically sorts PDFs, PPTs, images, and code files into separate directories without overwriting duplicate files.

# Folder Organizer Script

My Downloads and Desktop folders were always cluttered with random PDFs, college notes, screenshots, and code files, so I wrote this Python script to sort everything into proper folders automatically.

# What it does
- Opens a folder selection pop-up (using `tkinter`) so you don't have to hardcode file paths.
- Scans the selected folder and moves files into categories like `Images`, `Documents_And_Notes`, `Presentations`, `Coding_Files`, etc.
- Handles duplicate filenames (renames them to `file_1.pdf`, `file_2.pdf`, etc.) so nothing gets overwritten by mistake.

# How to use it
Make sure you have Python installed, then just run:

```bash
python organizer.py
