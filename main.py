from pathlib import Path
import os
import shutil


BASE_DIR = Path("Files-Folders")


def print_separator():
    print("-------------------------------------------")


def ensure_workspace():
    BASE_DIR.mkdir(parents=True, exist_ok=True)


def get_target(name):
    """Return a safe path inside the Files-Folders workspace."""
    name = name.strip()
    if not name:
        raise ValueError("Name cannot be empty.")

    target = (BASE_DIR / name).resolve()
    workspace = BASE_DIR.resolve()

    if target != workspace and workspace not in target.parents:
        raise ValueError("Path must stay inside the Files-Folders workspace.")

    return target


def readFileAndFolder():
    ensure_workspace()
    items = sorted(BASE_DIR.rglob("*"), key=lambda item: str(item).lower())

    if not items:
        print("Workspace is empty.")
    else:
        for i, item in enumerate(items, start=1):
            item_type = "DIR " if item.is_dir() else "FILE"
            print(f"{i} : [{item_type}] {item}")

    print_separator()


def createFile():
    try:
        readFileAndFolder()
        name = input("Enter new file name:- ")
        path = get_target(name)

        if path.exists():
            print("This file or folder already exists.")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            data = input("What you want to write in that file:- ")
            path.write_text(data, encoding="utf-8")
            print("FILE CREATED SUCCESSFULLY")
    except (OSError, ValueError) as err:
        print(f"An error occurred: {err}")

    print_separator()


def readFile():
    try:
        name = input("Enter file name you want to read:- ")
        path = get_target(name)

        if path.exists() and path.is_file():
            print("\n" + path.read_text(encoding="utf-8"))
            print("READ SUCCESSFULLY")
        else:
            print("File doesn't exist.")
    except (OSError, ValueError, UnicodeDecodeError) as err:
        print(f"An error occurred: {err}")

    print_separator()


def renameFile(path):
    try:
        new_name = input("Enter new name:- ")
        new_path = get_target(new_name)

        if new_path.exists():
            response = input("Destination exists. Overwrite it? (y/n):- ").strip().lower()
            if response != "y":
                print("RENAME CANCELLED")
                return

            if new_path.is_dir():
                print("Cannot overwrite a directory with a file.")
                return

            new_path.unlink()

        path.rename(new_path)
        print("RENAME SUCCESSFULLY")
    except (OSError, ValueError) as err:
        print(f"An error occurred: {err}")

    print_separator()


def overwriteFile(path):
    try:
        response = input("Overwrite existing data? (y/n):- ").strip().lower()
        if response != "y":
            print("OVERWRITE CANCELLED")
            print_separator()
            return

        data = input("Tell what you want to write; this will overwrite the data:- ")
        path.write_text(data, encoding="utf-8")
        print("OVERWRITE SUCCESSFULLY")
    except (OSError, ValueError) as err:
        print(f"An error occurred: {err}")

    print_separator()


def appendFile(path):
    try:
        data = input("Tell what you want to append:- ")
        with path.open("a", encoding="utf-8") as file:
            file.write(data)
        print("APPEND SUCCESSFULLY")
    except (OSError, ValueError) as err:
        print(f"An error occurred: {err}")

    print_separator()


def updateFile():
    readFileAndFolder()

    try:
        name = input("Enter file name you want to update:- ")
        path = get_target(name)

        if not path.exists() or not path.is_file():
            print("File doesn't exist.")
            print_separator()
            return

        print("Press 1 for rename")
        print("Press 2 for overwriting data")
        print("Press 3 for append data")

        response = get_menu_choice(3, "Enter your response:- ")

        if response == 1:
            renameFile(path)
        elif response == 2:
            overwriteFile(path)
        else:
            appendFile(path)
    except (OSError, ValueError) as err:
        print(f"An error occurred: {err}")
        print_separator()


def deleteFile():
    readFileAndFolder()

    try:
        print("Press 1 for remove file")
        print("Press 2 for remove folder")

        delete_type = get_menu_choice(2, "What you want to delete:- ")
        name = input("Enter which file/folder you want to delete:- ")
        path = get_target(name)

        if not path.exists():
            print("No such file or folder exists.")
            print_separator()
            return

        response = input(f"Confirm deletion of '{path}' (y/n):- ").strip().lower()
        if response != "y":
            print("DELETE CANCELLED")
            print_separator()
            return

        if delete_type == 1:
            if path.is_file():
                path.unlink()
                print("FILE REMOVED SUCCESSFULLY")
            else:
                print("Selected path is not a file.")
        elif delete_type == 2:
            if path.is_dir():
                shutil.rmtree(path)
                print("FOLDER REMOVED SUCCESSFULLY")
            else:
                print("Selected path is not a folder.")
    except (OSError, ValueError) as err:
        print(f"An error occurred: {err}")

    print_separator()


def copyFile():
    try:
        source_name = input("Enter source file name:- ")
        destination_name = input("Enter destination file name:- ")

        source = get_target(source_name)
        destination = get_target(destination_name)

        if not source.exists() or not source.is_file():
            print("Source file doesn't exist.")
        elif destination.exists():
            print("Destination already exists.")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            print("FILE COPIED SUCCESSFULLY")
    except (OSError, ValueError) as err:
        print(f"An error occurred: {err}")

    print_separator()


def moveFile():
    try:
        source_name = input("Enter source file/folder name:- ")
        destination_name = input("Enter destination file/folder name:- ")

        source = get_target(source_name)
        destination = get_target(destination_name)

        if not source.exists():
            print("Source file or folder doesn't exist.")
        elif destination.exists():
            print("Destination already exists.")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(destination))
            print("MOVE SUCCESSFULLY")
    except (OSError, ValueError) as err:
        print(f"An error occurred: {err}")

    print_separator()


def searchFiles():
    try:
        query = input("Enter file/folder name or text to search:- ").strip().lower()
        if not query:
            print("Search text cannot be empty.")
            print_separator()
            return

        ensure_workspace()
        matches = [item for item in BASE_DIR.rglob("*") if query in item.name.lower()]

        if matches:
            for item in matches:
                print(item)
            print(f"{len(matches)} match(es) found.")
        else:
            print("No matching files or folders found.")
    except OSError as err:
        print(f"An error occurred: {err}")

    print_separator()


def showMetadata():
    try:
        name = input("Enter file/folder name:- ")
        path = get_target(name)

        if not path.exists():
            print("File or folder doesn't exist.")
            print_separator()
            return

        stats = path.stat()
        item_type = "Directory" if path.is_dir() else "File"

        print(f"Path       : {path}")
        print(f"Type       : {item_type}")
        print(f"Size       : {stats.st_size} bytes")
        print(f"Modified   : {stats.st_mtime}")
        print(f"Permissions: {oct(stats.st_mode)[-3:]}")
    except (OSError, ValueError) as err:
        print(f"An error occurred: {err}")

    print_separator()


def get_menu_choice(maximum, prompt):
    while True:
        value = input(prompt).strip()
        try:
            choice = int(value)
            if 0 <= choice <= maximum:
                return choice
        except ValueError:
            pass

        print(f"Please enter a number between 0 and {maximum}.")


def main():
    ensure_workspace()

    while True:
        print("\n========== PYTHON FILE HANDLING ==========")
        print("1. Create a file")
        print("2. Read a file")
        print("3. Update a file")
        print("4. Delete a file/folder")
        print("5. List files and folders")
        print("6. Copy a file")
        print("7. Move a file/folder")
        print("8. Search files and folders")
        print("9. Show file/folder metadata")
        print("0. Exit")

        choice = get_menu_choice(9, "Please tell your response:- ")
        print_separator()

        if choice == 0:
            print("Thank you for using Python File Handling.")
            break
        elif choice == 1:
            createFile()
        elif choice == 2:
            readFile()
        elif choice == 3:
            updateFile()
        elif choice == 4:
            deleteFile()
        elif choice == 5:
            readFileAndFolder()
        elif choice == 6:
            copyFile()
        elif choice == 7:
            moveFile()
        elif choice == 8:
            searchFiles()
        elif choice == 9:
            showMetadata()


if __name__ == "__main__":
    main()
