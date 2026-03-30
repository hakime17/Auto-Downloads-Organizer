Auto Downloads Organizer

A simple Python script that automatically organizes files from your Downloads folder into system directories such as Music, Pictures, Documents, and Videos.

 Features

  Automatically sorts files by type
  Supports common file formats:

    Images (`.jpg`, `.png`, `.gif`)
    Music (`.mp3`, `.wav`, `.flac`)
    Documents (`.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`)
    Videos (`.mp4`, `.mkv`, `.mov`, `.avi`)
  Uses your system's default folders
  Lightweight and easy to run

How It Works
The script:
1. Scans your Downloads folder
2. Checks each file’s extension
3. Moves the file into the appropriate system folder
  Requirements

Python 3.x
Works on Windows, Linux, and macOS

  Usage
1. Clone the repository:
git clone https://github.com/yourusername/auto-downloads-organizer.git

2. Navigate into the folder:
cd auto-downloads-organizer

3. Run the script:
python main.py

Notes

* Make sure system folders like Music, Pictures, Documents, and Videos exist
* Files with duplicate names may be overwritten or skipped (future improvement)

Future Improvements

* Prevent file overwrites
* Add logging system
* GUI version
* Real-time file monitoring


Feel free to fork this project and improve it!
This project is open-source and available under the MIT License.
