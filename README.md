# Python File Handling

A beginner-friendly Python project that demonstrates common file and directory operations such as creating, reading, renaming, overwriting, appending, and deleting files from a dedicated `Files-Folders` directory.

This project is built using Python's built-in `pathlib` and `os` modules, making it a useful example for learners who want to understand practical file handling in Python.

## Overview

The application is a simple console-based menu program. When you run `main.py`, it prompts the user to choose an action and then performs the selected file operation.

The project is designed to help you practice:

- Creating files
- Reading file content
- Updating existing files
- Renaming files
- Appending data
- Deleting files
- Listing files and folders from a target directory

## Features

- Displays all files and folders inside `Files-Folders`
- Creates a new text file in the target directory
- Reads the contents of an existing file
- Renames a file
- Overwrites a file's content
- Appends new content to an existing file
- Deletes a file
- Uses an interactive terminal menu for easy use

## Project Structure

```text
Python-File-Heandling/
├── Files-Folders/
│   ├── Test.txt
│   └── test/
├── LICENSE
├── main.py
├── README.md
└── .gitignore (if present in your local clone)
```

## How the Program Works

The application uses a folder called `Files-Folders` as the working directory. All file operations are performed inside this folder.

### Menu options

When the script runs, it shows:

```python
Press 1 for creating a file
Press 2 for reading a file
Press 3 for updating a file
Press 4 for deletion a file
Press 0 for exit
```

### Example flow

1. Run the Python script
2. Select an action from the menu
3. Enter the required file name or file operation details
4. The script performs the operation and prints a success or error message

## Functions Included

The `main.py` file defines the following functions:

- `breakPrg()`
  - Exits the program

- `readFileAndFolder()`
  - Lists all files and directories under `Files-Folders`

- `createFile()`
  - Creates a new file and writes user-provided content

- `readFile()`
  - Reads and prints the content of an existing file

- `renameFile(p)`
  - Renames a file

- `overwriteFile(p)`
  - Replaces the file content with new content

- `appendFile(p)`
  - Adds new text to the end of the file

- `updateFile()`
  - Lets the user choose between rename, overwrite, or append actions

- `deleteFile()`
  - Removes an existing file

## Running the Project

Make sure Python is installed on your system.

### Step 1: Open terminal

Navigate to the project directory:

```bash
cd Python-File-Heandling
```

### Step 2: Run the script

```bash
python main.py
```

If you are using Python 3 specifically:

```bash
python3 main.py
```

## Example Usage

### Create a file

- Choose option `1`
- Enter the new file name
- Type content to write into the file

### Read a file

- Choose option `2`
- Enter the file name
- The file contents will be displayed in the console

### Update a file

- Choose option `3`
- Enter the file name
- Select one of the following:
  - `1` = Rename file
  - `2` = Overwrite content
  - `3` = Append content

### Delete a file

- Choose option `4`
- Enter the file name to remove

## File Handling Notes

This project is useful for learning how to:

- work with relative paths using `Path('Files-Folders') / name`
- handle file existence checks with `exists()` / `is_file()`
- read and write files with Python
- perform simple CRUD-like operations for files

## Requirements

- Python 3.x
- No external libraries are required

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Summary

This repository is a simple educational Python project for practicing file operations in a real-world scripting environment. It is ideal for beginners learning how files are created, updated, and deleted in Python.

If you want, I can also help you create a more polished version of this project with:

- better input validation
- a proper menu loop
- file extension checks
- error-handling improvements
- a more professional README and project structure
