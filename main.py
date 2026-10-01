from file_manager import (
    WORKSPACE,
    FileManagerError,
    append_file,
    copy_item,
    create_file,
    delete_file,
    delete_folder,
    get_metadata,
    list_items,
    move_item,
    overwrite_file,
    read_file,
    rename_file,
    search_items,
)


def show_items() -> None:
    WORKSPACE.mkdir(parents=True, exist_ok=True)
    items = list_items()
    if not items:
        print("Workspace is empty.")
    else:
        for index, item in enumerate(items, start=1):
            item_type = "DIR" if item.is_dir() else "FILE"
            relative = item.relative_to(WORKSPACE)
            print(f"{index} : [{item_type}] {relative}")
    print("-" * 43)


def prompt_non_empty(message: str) -> str:
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def prompt_choice(message: str, choices: set[int]) -> int:
    while True:
        try:
            value = int(input(message).strip())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if value in choices:
            return value
        print(f"Invalid choice. Select one of: {', '.join(map(str, sorted(choices)))}")


def confirm(message: str) -> bool:
    return input(f"{message} (y/n): ").strip().lower() == "y"


def report_error(error: Exception) -> None:
    print(f"Error: {error}")
    print("-" * 43)


def create() -> None:
    show_items()
    name = prompt_non_empty("Enter new file name/path: ")
    content = input("What do you want to write in that file: ")
    try:
        create_file(name, content)
        print("FILE CREATED SUCCESSFULLY")
    except (OSError, ValueError, FileManagerError) as error:
        report_error(error)


def read() -> None:
    name = prompt_non_empty("Enter file name/path you want to read: ")
    try:
        print(read_file(name))
        print("READ SUCCESSFULLY")
    except (OSError, ValueError, FileManagerError) as error:
        report_error(error)


def update() -> None:
    show_items()
    name = prompt_non_empty("Enter file name/path you want to update: ")
    choice = prompt_choice(
        "Press 1 for rename, 2 for overwrite, 3 for append: ", {1, 2, 3}
    )

    try:
        if choice == 1:
            new_name = prompt_non_empty("Enter new name/path: ")
            overwrite = False
            if (WORKSPACE / new_name).exists():
                overwrite = confirm("Destination exists. Overwrite it?")
            rename_file(name, new_name, overwrite=overwrite)
            print("RENAMED SUCCESSFULLY")
        elif choice == 2:
            content = input("Enter replacement content: ")
            if not confirm("Replace the existing file content?"):
                print("Operation cancelled.")
                return
            overwrite_file(name, content)
            print("OVERWRITE SUCCESSFULLY")
        else:
            content = input("Enter content to append: ")
            append_file(name, content)
            print("APPEND SUCCESSFULLY")
    except (OSError, ValueError, FileManagerError) as error:
        report_error(error)


def delete() -> None:
    show_items()
    choice = prompt_choice("Press 1 for remove file, 2 for remove folder: ", {1, 2})
    name = prompt_non_empty("Enter file/folder path to delete: ")

    try:
        if not confirm(f"Delete '{name}' permanently?"):
            print("Operation cancelled.")
            return

        if choice == 1:
            delete_file(name)
        else:
            delete_folder(name)
        print("REMOVED SUCCESSFULLY")
    except (OSError, ValueError, FileManagerError) as error:
        report_error(error)


def copy_or_move() -> None:
    choice = prompt_choice("Press 1 for copy, 2 for move: ", {1, 2})
    source = prompt_non_empty("Enter source path: ")
    destination = prompt_non_empty("Enter destination path: ")

    try:
        overwrite = False
        if (WORKSPACE / destination).exists():
            overwrite = confirm("Destination exists. Overwrite it?")
        if choice == 1:
            copy_item(source, destination, overwrite=overwrite)
            print("COPIED SUCCESSFULLY")
        else:
            move_item(source, destination, overwrite=overwrite)
            print("MOVED SUCCESSFULLY")
    except (OSError, ValueError, FileManagerError) as error:
        report_error(error)


def search() -> None:
    pattern = prompt_non_empty("Enter filename/pattern (e.g. *.txt): ")
    try:
        matches = search_items(pattern)
        if not matches:
            print("No matching files or folders found.")
        else:
            for item in matches:
                kind = "DIR" if item.is_dir() else "FILE"
                print(f"[{kind}] {item.relative_to(WORKSPACE)}")
            print(f"{len(matches)} match(es) found.")
    except (OSError, ValueError, FileManagerError) as error:
        report_error(error)


def metadata() -> None:
    name = prompt_non_empty("Enter file/folder path: ")
    try:
        details = get_metadata(name)
        for key, value in details.items():
            print(f"{key.title():<10}: {value}")
    except (OSError, ValueError, FileManagerError) as error:
        report_error(error)


def main() -> None:
    while True:
        print("1. Create file")
        print("2. Read file")
        print("3. Update file")
        print("4. Delete file/folder")
        print("5. Copy file/folder")
        print("6. Move file/folder")
        print("7. Search files/folders")
        print("8. View metadata")
        print("0. Exit")

        choice = prompt_choice("Please enter your choice: ", set(range(9)))
        print("-" * 43)

        if choice == 0:
            print("Goodbye.")
            break
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5 or choice == 6:
            copy_or_move()
        elif choice == 7:
            search()
        elif choice == 8:
            metadata()


if __name__ == "__main__":
    main()
