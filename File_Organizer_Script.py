import os
import shutil
from datetime import datetime

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Data": [".json", ".xml", ".csv"],
    "Others": []
}

folder_path = input("Enter folder path: ").strip()
if not folder_path:
    print("No folder path entered.")
    raise SystemExit(1)

folder_path = os.path.abspath(folder_path)
if not os.path.isdir(folder_path):
    print(f"Path is not a valid folder: {folder_path}")
    raise SystemExit(1)

dry_run_input = input("Dry Run? (yes/no): ").strip().lower()
dry_run = dry_run_input in {"yes", "y", "true", "1"}

log_file_path = os.path.join(folder_path, "organizer_log.txt")
script_path = os.path.abspath(__file__)

moved_count = 0
skipped_count = 0

for file in os.listdir(folder_path):

    full_path = os.path.join(folder_path, file)

    if not os.path.isfile(full_path) or os.path.abspath(full_path) in {log_file_path, script_path}:
        skipped_count += 1
        continue

    file_extension = os.path.splitext(file)[1].lower()

    destination_folder_name = "Others"

    for category in FILE_CATEGORIES:

        if file_extension in FILE_CATEGORIES[category]:
            destination_folder_name = category
            break

    destination_folder_path = os.path.join(folder_path, destination_folder_name)

    if not os.path.exists(destination_folder_path):

        if not dry_run:
            os.makedirs(destination_folder_path, exist_ok=True)

    destination_file_path = os.path.join(destination_folder_path, file)

    if os.path.exists(destination_file_path):

        base_name, extension = os.path.splitext(file)

        counter = 1

        while True:

            new_name = base_name + "(" + str(counter) + ")" + extension

            new_path = os.path.join(destination_folder_path, new_name)

            if not os.path.exists(new_path):

                destination_file_path = new_path
                break

            counter += 1

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_message = (
        current_time
        + " | "
        + full_path
        + " --> "
        + destination_file_path
    )

    if dry_run:

        print("Would move:")
        print(full_path)
        print(" --> ")
        print(destination_file_path)
        print()

    else:

        shutil.move(full_path, destination_file_path)
        moved_count += 1

        print("Moved:")
        print(full_path)
        print(" --> ")
        print(destination_file_path)
        print()

        with open(log_file_path, "a") as log_file:
            log_file.write(log_message + "\n")

print("File organization completed.")
print(f"Summary: moved {moved_count} file(s), skipped {skipped_count} non-file item(s).")
print(f"Log file: {log_file_path}")

# Scheduling examples:
# - Windows Task Scheduler: run this script daily with python "C:\\path\\to\\File_Organizer_Script.py"
# - Linux cron: 0 10 * * * /usr/bin/python3 /path/to/File_Organizer_Script.py