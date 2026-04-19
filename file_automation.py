# Python File Handling & Automation Script
# This script demonstrates reading, writing, renaming, moving, and deleting files
# along with exception handling using try-except.

import os
import shutil

try:
    # 1. Writing data to a text file
    print("Creating and writing to file...")

    with open("sample.txt", "w") as file:
        file.write("This is a sample file created using Python.\n")
        file.write("This demonstrates file handling operations.\n")

    print("File written successfully.\n")

    # 2. Reading data from the file
    print("Reading file content...")

    with open("sample.txt", "r") as file:
        content = file.read()
        print("File Content:\n", content)

    # 3. Renaming the file
    print("Renaming file...")

    os.rename("sample.txt", "renamed_sample.txt")
    print("File renamed to renamed_sample.txt\n")

    # 4. Moving the file to a folder
    folder_name = "processed_files"

    # Create folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    shutil.move("renamed_sample.txt", f"{folder_name}/renamed_sample.txt")
    print("File moved to processed_files folder.\n")

    # 5. Deleting the file
    file_path = f"{folder_name}/renamed_sample.txt"

    os.remove(file_path)
    print("File deleted successfully.\n")

except FileNotFoundError:
    print("Error: The file was not found.")

except PermissionError:
    print("Error: Permission denied while accessing the file.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("File handling operations completed.")