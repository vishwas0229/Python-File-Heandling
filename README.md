# 🐍 Python File Handling

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Project Type](https://img.shields.io/badge/Project-CLI-orange)

**A learning-focused command-line project for understanding Python file and folder handling.**

> A simple, menu-driven Python command-line application for learning and practicing file and folder operations using Python's standard library.

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Objectives](#-objectives)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Main Menu](#-main-menu)
- [Workflow](#-program-workflow)
- [Functions](#-functions-in-mainpy)
- [Concepts Demonstrated](#-file-handling-concepts-demonstrated)
- [Requirements](#-functional-requirements)
- [Testing](#-test-scenarios)
- [How to Run](#️-how-to-run)
- [Current Implementation](#️-current-implementation-notes)
- [Planned Improvements](#-planned-improvements)
- [Project Report](#-detailed-project-report)

---

## 📌 Project Overview

**Python File Handling** is a beginner-friendly CLI application that performs common filesystem operations inside the `Files-Folders` workspace.

The current `main.py` provides:

- 📂 Recursive file and folder listing
- 📝 File creation with initial content
- 📖 File reading
- ✏️ File update operations
- 🔄 File renaming
- 🧹 File overwriting
- ➕ File appending
- 🗑️ File deletion
- 📁 Folder deletion
- 🔁 Continuous menu navigation
- 🚪 Program exit

The application is implemented in a single **`main.py`** file and uses the Python standard library. No third-party packages are required.

---

# 🎯 Objectives

This project is intended to provide practical understanding of:

1. File and directory handling in Python.
2. Creating, reading, writing, and appending text files.
3. Renaming and deleting filesystem items.
4. Building paths with `pathlib.Path`.
5. Recursively listing files and directories with `rglob()`.
6. Using functions to organize a CLI application.
7. Using `try-except` for basic error handling.
8. Building a repeated command-line menu with user input.

---

# ✨ Features

## 📂 1. List Files and Folders

`readFileAndFolder()` scans the `Files-Folders` directory recursively:

```python
Path("Files-Folders").rglob("*")
```

Every discovered item is printed with a number.

## 📝 2. Create a File

`createFile()`:

1. Displays the current workspace.
2. Requests a file name.
3. Checks whether the path already exists.
4. Creates the file using write mode.
5. Writes user-provided content.

## 📖 3. Read a File

`readFile()` checks that the selected path exists and is a file, then reads and displays its contents.

## ✏️ 4. Update a File

`updateFile()` provides three operations:

| Option | Operation | Purpose |
|---:|---|---|
| 1 | Rename | Change the file name |
| 2 | Overwrite | Replace existing content |
| 3 | Append | Add content to the existing file |

## 🔄 5. Rename a File

`renameFile()` uses `Path.rename()`. If the destination already exists, the user is asked for confirmation before attempting the rename.

## 🧹 6. Overwrite File

`overwriteFile()` opens the file using write mode:

```python
open(p, "w")
```

This replaces the previous content.

> ⚠️ The current implementation does not request a separate confirmation before overwriting file content.

## ➕ 7. Append Data

`appendFile()` opens the file in append mode:

```python
open(p, "a")
```

The current implementation adds a leading space before the supplied text.

## 🗑️ 8. Delete File or Folder

`deleteFile()` supports:

- **Option 1:** Remove a file.
- **Option 2:** Remove a folder recursively.

The user is asked for confirmation before the removal operation.

## 🔁 9. Continuous Menu

The main program uses:

```python
while 1:
```

so the menu continues until the user selects `0`.

---

# 🧰 Technologies Used

| Technology / Module | Usage |
|---|---|
| **Python 3** | Core programming language |
| **pathlib** | Path construction, recursive traversal, existence checks, file checks, renaming |
| **os** | File removal |
| **shutil** | Recursive folder removal |
| **File I/O** | Reading, writing, overwriting, appending |
| **Git / GitHub** | Version control and project hosting |

### Dependencies

No third-party Python packages are required.

---

# 🗂️ Project Structure

```text
Python-File-Heandling/
│
├── Files-Folders/
│   ├── Test.txt
│   └── test/
│       └── test.txt
│
├── main.py
├── README.md
└── LICENSE
```

---

# 🧭 Main Menu

The current `main.py` displays:

```text
Press 1 for creating a file
Press 2 for reading a file
Press 3 for updating a file
Press 4 for deletion a file
Press 0 for exit
```

### Update Menu

```text
Press 1 for rename
Press 2 for overwriting data
Press 3 for append data
```

### Delete Menu

```text
Press 1 for remove file
Press 2 for remove folder
```

---

# 🔄 Program Workflow

```text
                              START
                                │
                                ▼
                         ┌─────────────┐
                         │  Main Menu  │
                         └──────┬──────┘
                                │
       ┌───────────────┐────────┼────────┐───────────────────┐
       ▼               ▼                 ▼                   ▼
    Create            Read             Update              Delete
       │               │          ┌───────┼───────┐          |
       │               │          ▼       ▼       ▼          |
       │               │       Rename Overwrite Append       |
       │               │          │       │       │          |
       └───────────────┴──────────┴───────┴───────┴──────────┘
                                 │
                                 ▼
                          Return to Menu
                                 │
                            ┌────┴────┐
                            │ Exit 0  │
                            └─────────┘
```

---

# 🧩 Functions in `main.py`

| Function | Responsibility |
|---|---|
| `readFileAndFolder()` | Recursively lists workspace items |
| `createFile()` | Creates a file and writes initial content |
| `readFile()` | Reads file contents |
| `renameFile(p)` | Renames a file |
| `overwriteFile(p)` | Replaces file contents |
| `appendFile(p)` | Appends content |
| `updateFile()` | Selects rename, overwrite, or append |
| `deleteFile()` | Removes a file or folder |

The main program loop handles menu selection and dispatches the selected operation.

---

# 📚 File Handling Concepts Demonstrated

## File Modes

| Mode | Meaning | Usage |
|---|---|---|
| `r` | Read | Reading file contents |
| `w` | Write | Creating/overwriting content |
| `a` | Append | Adding content |

## Path Handling

The project constructs paths with:

```python
Path("Files-Folders") / name
```

## Recursive Traversal

```python
path.rglob("*")
```

is used to discover nested files and directories.

## File and Folder Operations

```text
Create
  ↓
Read
  ↓
Update → Rename / Overwrite / Append
  ↓
Delete File / Delete Folder
```

---

# 🏗️ Technical Architecture

The application follows a simple procedural CLI architecture:

```text
                 USER
                   │
                   ▼
              MAIN MENU
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
    CREATE        READ       UPDATE
       │           │           │
       │           │      ┌────┼────┐
       │           │      ▼    ▼    ▼
       │           │   RENAME OVERWRITE APPEND
       │           │      │    │    │
       └───────────┴──────┴────┴────┘
                   │
                   ▼
             DELETE FILE/FOLDER
                   │
                   ▼
              FILESYSTEM
          Files-Folders/
```

There is no database, GUI, web server, external API, authentication system, or third-party package.

---

# 📋 Functional Requirements

1. Display files and folders in the workspace.
2. Create a new file.
3. Write initial file content.
4. Read an existing file.
5. Rename a file.
6. Overwrite file content.
7. Append content.
8. Delete a file.
9. Delete a folder recursively.
10. Continue displaying the menu after each operation.
11. Exit when the user selects `0`.
12. Display success, invalid-input, or error messages.

---

# ⚙️ Non-Functional Requirements

### Usability
The application uses simple numbered menu choices.

### Portability
Only Python's standard library is required.

### Maintainability
Filesystem operations are separated into functions.

### Simplicity
The project remains a compact, single-file educational CLI.

---

# 🧪 Test Scenarios

| # | Scenario | Expected Result |
|---:|---|---|
| 1 | Create a new file | File is created and content is written |
| 2 | Create an existing file | Existing-path message is shown |
| 3 | Read an existing file | Content is displayed |
| 4 | Rename a file | File is renamed when destination is available |
| 5 | Rename to an existing destination | User receives an overwrite prompt |
| 6 | Overwrite a file | Existing content is replaced |
| 7 | Append content | New content is added |
| 8 | Delete a file and confirm | File is removed |
| 9 | Delete a folder and confirm | Folder and its contents are removed |
| 10 | Select an invalid numeric menu option | `INVALID INPUT` is displayed |
| 11 | Enter non-numeric menu input | Current implementation can raise `ValueError` |
| 12 | Select `0` | Program exits |

---

# ▶️ How to Run

## Prerequisite

Install Python 3.x:

```bash
python --version
```

or:

```bash
python3 --version
```

## Clone

```bash
git clone https://github.com/vishwas0229/Python-File-Heandling.git
cd Python-File-Heandling
```

## Run

```bash
python main.py
```

or:

```bash
python3 main.py
```

---

# 💡 Example Usage

### Create

```text
Press 1 for creating a file
Please tell your response :- 1

Enter new file name:- demo.txt
What you want to write in that file:- Hello Python
FILE CREATED SUCCESSFULLY
```

### Read

```text
Press 2 for reading a file
Please tell your response :- 2

Enter file name you want to read:- demo.txt
Hello Python
READ SUCCESSFULLY
```

### Update → Append

```text
Press 3 for updating a file
Please tell your response :- 3

Enter file name you want to update:- demo.txt
Press 1 for rename
Press 2 for overwriting data
Press 3 for append data
Enter your responce:- 3

Tell what you want to append:- Again!
APPEND SUCCESSFULLY
```

### Delete

```text
Press 4 for deletion a file
Please tell your response :- 4

Press 1 for remove file
Press 2 for remove folder
What you want to delete:- 1
Enter which file/folder you want to delete:- demo.txt
You want to delete this file (y):- y
REMOVE SUCCESSFULLY
```

---

# 🔐 Safety and Data Considerations

This application performs real filesystem changes.

- Overwrite replaces existing file contents.
- Delete can permanently remove files.
- Folder deletion is recursive.
- Rename can replace an existing destination after confirmation.
- The current program does not restrict paths to the `Files-Folders` workspace.
- The application does not provide backup, undo, or version history.

Use disposable test data while learning.

---

# ⚠️ Current Implementation Notes

The following points are based directly on the current `main.py`:

### 1. Continuous menu is implemented

The application uses a `while 1` loop and returns to the menu after operations.

### 2. Input validation is basic

Menu values are converted with `int(input(...))). Non-numeric input can raise `ValueError`.

### 3. Some path checks need correction

`readFile()` correctly uses:

```python
p.exists()
```

but `renameFile()` contains:

```python
if not newP.exists():
```

which should be reviewed against the intended destination-existence logic.

### 4. Some exception messages need improvement

Several handlers correctly use f-strings, while `updateFile()` contains:

```python
print("An error occured as {err}")
```

so the actual exception is not interpolated there.

### 5. Path validation is not implemented

User-supplied names are joined directly with `Files-Folders`. There is currently no explicit protection against path traversal.

### 6. Naming and spelling can be cleaned up

Examples include:

- `dosen't`
- `responce`
- `breakPrg` is absent in the current code because the loop exits directly.
- Several messages use inconsistent grammar.

### 7. The project focuses on text files

The current implementation uses normal text-file I/O and does not provide special binary-file processing.

---

# 📌 Repository Roadmap

The repository uses GitHub Issues to track improvements separately from the current implementation. The roadmap intentionally distinguishes **what exists in `main.py`** from **what is planned**.

### Current Implementation

- ✅ Create and read text files
- ✅ Rename files
- ✅ Overwrite and append content
- ✅ Delete files and folders
- ✅ Recursive workspace listing
- ✅ Continuous CLI menu

### Planned Improvements

The repository tracks the following improvements through GitHub Issues:

- Correct all `Path.exists()` checks.
- Improve exception reporting.
- Add robust numeric input validation.
- Add safer filename/path validation.
- Add copy and move operations.
- Add file search.
- Add metadata inspection.
- Add automated tests.
- Refactor the single-file application into smaller modules.
- Standardize CLI messages and naming.

---

# 📝 Detailed Project Report

## 1. Introduction

File handling is a fundamental programming concept because applications frequently need to store, retrieve, modify, rename, and remove filesystem data.

This project combines these concepts into a single interactive Python CLI application.

## 2. Problem Statement

Beginners often learn file functions individually but may not understand how different filesystem operations work together.

This project provides a practical menu-driven environment for experimenting with common file and folder operations.

## 3. Proposed Solution

The application uses `Files-Folders/` as its working directory and provides separate functions for listing, creation, reading, updating, and deletion.

A continuous main menu allows repeated operations during one execution.

## 4. Scope

### In Scope

- Recursive file/folder listing
- File creation
- File reading
- File renaming
- File overwrite
- File append
- File deletion
- Folder deletion
- CLI interaction
- Basic exception handling

### Out of Scope

- Database management
- Cloud storage
- Remote filesystem access
- Authentication
- Multi-user concurrency
- File versioning
- Encryption
- GUI
- Advanced binary-file processing

## 5. Inputs

- Main menu selection
- File/folder name
- File content
- Replacement content
- Appended content
- New filename
- Delete type
- Confirmation response

## 6. Outputs

- Workspace listing
- File contents
- Success messages
- Invalid-input messages
- Error messages

## 7. Data Flow

```text
User
  │
  ▼
Main Menu
  │
  ├── Create ──► Build Path ──► Write File
  ├── Read ────► Build Path ──► Read File
  ├── Update ──► Rename / Overwrite / Append
  └── Delete ──► Build Path ──► Remove File/Folder
  │
  ▼
Console Result
  │
  ▼
Return to Main Menu
```

## 8. Error Handling

The project uses `try-except` around several filesystem operations. Future improvements can replace broad exception handling with specific exceptions such as `FileNotFoundError`, `PermissionError`, `IsADirectoryError`, and `ValueError`.

## 9. Benefits

- Easy for beginners to understand.
- Demonstrates multiple filesystem operations.
- Uses only Python's standard library.
- Provides hands-on CLI practice.
- Creates a foundation for a larger file-management utility.

## 10. Limitations

The current implementation is educational and does not provide production-grade path security, backup, undo, logging, automated testing, or advanced input validation.

## 11. Conclusion

**Python File Handling** provides a practical introduction to filesystem programming in Python. It demonstrates listing, creation, reading, updating, renaming, overwriting, appending, and deletion through a continuous command-line interface.

Further improvements are tracked transparently through the repository's GitHub Issues.

---

# 👨‍💻 Author

**Vishwas**

GitHub: [@vishwas0229](https://github.com/vishwas0229)

Repository: [Python-File-Heandling](https://github.com/vishwas0229/Python-File-Heandling)

---

# 📄 License

This project is licensed under the **MIT License**. See the [`LICENSE`](LICENSE) file for details.

---

⭐ **Learning-focused Python project for understanding file and folder handling through a command-line application.**
