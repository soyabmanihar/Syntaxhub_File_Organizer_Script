# 📂 File Organizer Script

A Python automation script that organizes files in a folder into category-based subfolders such as Images, Videos, Documents, Audio, Archives, Data, and Others based on file extensions.

The script supports:
- ✔️ Automatic file categorization
- ✔️ Dry Run mode
- ✔️ Duplicate file handling
- ✔️ Logging moved files
- ✔️ Automatic folder creation

---

# ✨ Features

- Organizes files by extension
- Creates folders automatically
- Handles duplicate filenames safely
- Supports Dry Run mode for testing
- Generates log file with timestamps
- Skips invalid items and directories

---

# 🗂️ Supported Categories

| Category | Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff` |
| Videos | `.mp4`, `.mkv`, `.flv`, `.avi`, `.mov` |
| Documents | `.pdf`, `.doc`, `.docx`, `.txt`, `.ppt`, `.pptx`, `.xls`, `.xlsx` |
| Audio | `.mp3`, `.wav`, `.aac`, `.flac` |
| Archives | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Data | `.json`, `.xml`, `.csv` |
| Others | Unknown file types |

---

# ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/file-organizer.git
```

Run the script:

```bash
python organizer.py
```

Example:

```text
Enter folder path: C:\Users\Username\Downloads
Dry Run? (yes/no): yes
```

---

# 🔍 Dry Run Example

```text
Would move:
C:\Downloads\image.jpg
 -->
C:\Downloads\Images\image.jpg
```

| Input | Action |
|---|---|
| `yes` | Preview changes only |
| `no` | Actually move files |

---

# 📝 Logging

Moved files are saved in:

```text
organizer_log.txt
```

Example:

```text
2026-05-07 20:30:15 | C:\Downloads\song.mp3 --> C:\Downloads\Audio\song.mp3
```

---

# 📸 Example

## Before

```text
Downloads/
├── image.jpg
├── song.mp3
├── notes.pdf
```

## After

```text
Downloads/
├── Images/
├── Audio/
├── Documents/
```

---

# 📋 Requirements

- Python 3.x
- No external libraries required

---

# 👨‍💻 Author

Developed by Soyab

---

# 📜 License

This project is open-source and available for educational and personal use.
