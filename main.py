import os
import shutil

current_dr = os.path.join(os.path.expanduser("~"), "Downloads")

Destinations = {
    "Pictures": (
        ".jpg",
        ".png",
        ".gif",
    ),
    "Music": (".mp3", ".wav", ".flac"),
    "Documents": (".pdf", ".docx", ".txt", ".xlsx", ".pptx"),
    "Videos": (".mp4", ".mkv", ".mov", ".avi"),
}

for folder_name, extensions in Destinations.items():
    Destination_dr = os.path.join(os.path.expanduser("~"), folder_name)

    for file in os.listdir(current_dr):
        file_path = os.path.join(current_dr, file)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file)[1].lower()

            if extension in extensions:
                shutil.move(file_path, os.path.join(Destination_dr, file))
