# 🐍 Python File Handling

> A simple, menu-driven Python command-line program for learning and practicing file and folder operations with Python's standard library.

## 📌 Project Overview

**Python File Handling** is a beginner-friendly console application that demonstrates how Python can interact with the local filesystem.

The program uses a dedicated `Files-Folders` directory as its working area and provides a menu through which the user can:

- List files and folders recursively
- Create a new file
- Read file contents
- Update an existing file
- Rename a file
- Overwrite file contents
- Append content to a file
- Delete a file
- Exit the program

The project is implemented in a single **`main.py`** file and uses Python's built-in **`pathlib`** and **`os`** modules. No third-party packages are required.

---

# 🎯 Objectives

The project is designed to provide practical understanding of:

1. File and directory handling in Python.
2. Creating and reading text files.
3. Writing, overwriting, and appending file data.
4. Renaming and deleting files.
5. Building filesystem paths with `pathlib.Path`.
6. Recursively discovering files and directories with `rglob()`.
7. Using functions to organize a small Python program.
8. Using `try-except` blocks for basic runtime error handling.
9. Building a simple command-line interface using user input.

---

# ✨ Features

## 📂 1. List Files and Folders

The program scans the `Files-Folders` directory recursively and prints every discovered file and directory.

It uses:

```python
Path('Files-Folders').rglob('*')
```

This lets the user inspect the available items before performing file operations.

## 📝 2. Create a File

The **Create File** option displays the workspace, asks for a file name, checks whether the target already exists, creates the file, and writes user-provided text.

Example:

```text
Enter new file name:- notes.txt
What you want to write in that file:- Learning Python file handling.
FILE CREATED SUCCESSFULLY
```

## 📖 3. Read a File

The **Read File** option asks for a file name and attempts to display its complete contents using read mode:

```python
open(p, "r")
```

## ✏️ 4. Update a File

The **Update File** option provides three operations:

| Option | Operation | Purpose |
|---:|---|---|
| `1` | Rename | Changes the file name |
| `2` | Overwrite | Replaces existing file contents |
| `3` | Append | Adds new content at the end |

## 🔄 5. Rename a File

The rename operation requests a new name and uses `Path.rename()` to move the file to the new path. The current code also asks for confirmation when the destination path already exists.

## 🧹 6. Overwrite File Content

The selected file is opened using write mode:

```python
open(p, "w")
```

Write mode replaces the previous content.

> ⚠️ Use this operation carefully because the previous file content is replaced.

## ➕ 7. Append Data

The selected file is opened in append mode:

```python
open(p, "a")
```

The new text is added after the existing content. The current implementation inserts one leading space before the appended text.

## 🗑️ 8. Delete a File

The main menu includes option `4` for deletion. `deleteFile()` validates that the target is a file and removes it with:

```python
os.remove(p)
```

## 🚪 9. Exit

Selecting `0` calls `breakPrg()`, which simply returns.

---

# 🧰 Technologies Used

| Technology / Module | Usage |
|---|---|
| **Python 3** | Core programming language |
| **pathlib** | Path construction, recursive traversal, file checks, and renaming |
| **os** | File removal |
| **File I/O** | Reading, writing, overwriting, and appending |
| **Git / GitHub** | Source-code management and project hosting |

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

### Repository Components

| Component | Description |
|---|---|
| `Files-Folders/` | Working directory used by the program |
| `main.py` | Complete application logic |
| `README.md` | Project documentation |
| `LICENSE` | MIT License |

---

# 🧭 Main Menu

The current `main.py` displays:

```text
Press 1 for creating a file
Press 2 for reading a file
Press 3 for updating a file
Press 4 for deletion a file
Press 0 for exit
Please tell your response :-
```

The update submenu is:

```text
Press 1 for rename
Press 2 for overwriting data
Press 3 for append data
Enter your responce:-
```

---

# 🔄 Program Workflow

```text
                    ┌─────────────────────┐
                    │     Start Program   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Display Menu     │
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼─────────────────────┐
          │                    │                     │
          ▼                    ▼                     ▼
      Create File           Read File            Update File
          │                    │                     │
          │                    │          ┌──────────┼──────────┐
          │                    │          │          │          │
          │                    │          ▼          ▼          ▼
          │                    │       Rename    Overwrite    Append
          │                    │          │          │          │
          └────────────────────┴──────────┴──────────┴──────────┐
                                                                 │
                                                                 ▼
                                                            Delete File
                                                                 │
                                                                 ▼
                                                            Program End
```

The top-level menu is currently displayed once per execution. There is no continuous `while` loop around the menu.

---

# 🧩 Functions in `main.py`

| Function | Responsibility |
|---|---|
| `breakPrg()` | Provides the exit branch |
| `readFileAndFolder()` | Recursively lists workspace items |
| `createFile()` | Creates a file and writes initial content |
| `readFile()` | Reads and prints file content |
| `renameFile(p)` | Renames a selected file |
| `overwriteFile(p)` | Replaces file content |
| `appendFile(p)` | Adds content to an existing file |
| `updateFile()` | Selects rename, overwrite, or append |
| `deleteFile()` | Removes a selected file |

---

# 📚 File Handling Concepts Demonstrated

## File Modes

| Mode | Meaning | Use in Project |
|---|---|---|
| `r` | Read | Read file contents |
| `w` | Write / overwrite | Create or replace content |
| `a` | Append | Add content to an existing file |

## `pathlib.Path`

Paths are constructed with expressions such as:

```python
p = Path('Files-Folders') / name
```

## Recursive Traversal

`rglob('*')` recursively discovers files and directories below `Files-Folders`.

## Functions and Control Flow

The program uses functions, `if` / `elif` / `else`, user input, loops inside library operations, and exception handling to organize its behavior.

## Exception Handling

Several file operations use:

```python
try:
    ...
except Exception as err:
    ...
```

---

# 🏗️ Technical Architecture

The application follows a small procedural CLI architecture:

```text
                 USER
                   │
                   ▼
             CLI MAIN MENU
                   │
       ┌───────────┼───────────┐
       │           │           │
       ▼           ▼           ▼
    CREATE       READ       UPDATE
       │           │           │
       │           │       ┌───┼─────────┐
       │           │       │   │         │
       │           │       ▼   ▼         ▼
       │           │    RENAME OVERWRITE APPEND
       │           │       │    │         │
       └───────────┴───────┴────┴─────────┘
                               │
                               ▼
                            DELETE
                               │
                               ▼
                         FILESYSTEM
                     (Files-Folders/)
```

The project has no database, web server, GUI, external API, or third-party Python dependency.

---

# 📋 Functional Requirements

1. Display files and directories in the working folder.
2. Create a new file.
3. Write initial text to a file.
4. Read an existing file.
5. Rename a file.
6. Overwrite file content.
7. Append additional content.
8. Delete an existing file.
9. Exit through the command-line menu.
10. Display operation status or error messages.

---

# ⚙️ Non-Functional Requirements

### Usability
The application exposes straightforward numeric choices through the terminal.

### Portability
The implementation relies on Python's standard library.

### Maintainability
File operations are separated into functions with specific responsibilities.

### Simplicity
The code remains compact so the underlying filesystem concepts are easy to study.

---

# 🧪 Test Cases

| # | Scenario | Expected Result |
|---:|---|---|
| 1 | Select `1` and enter a new file name | File is created and content is written |
| 2 | Create using an existing path | Existing-file message is shown |
| 3 | Select `2` and enter an existing file | File content is displayed |
| 4 | Select `3 → 1` | File is renamed |
| 5 | Select `3 → 2` | Existing content is replaced |
| 6 | Select `3 → 3` | New content is appended |
| 7 | Select `4` and enter an existing file | File is removed |
| 8 | Select `0` | Program exits |
| 9 | Enter unsupported numeric menu input | `INVALID INPUT` is displayed |
| 10 | Enter non-numeric input where `int()` is expected | `ValueError` can occur |

---

# ▶️ How to Run

## Prerequisite

Install **Python 3.x**.

Check the installation:

```bash
python --version
```

or:

```bash
python3 --version
```

## 1. Clone the Repository

```bash
git clone https://github.com/vishwas0229/Python-File-Heandling.git
```

## 2. Enter the Project Directory

```bash
cd Python-File-Heandling
```

## 3. Run the Program

```bash
python main.py
```

or:

```bash
python3 main.py
```

---

# 💡 Example Usage

## Create a File

```text
Press 1 for creating a file
Please tell your response :- 1

Enter new file name:- demo.txt
What you want to write in that file:- Hello Python
FILE CREATED SUCCESSFULLY
```

## Read a File

```text
Press 2 for reading a file
Please tell your response :- 2

Enter file name you want to read:- demo.txt
Hello Python
READ SUCCESSFULLY
```

## Update → Append

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

## Delete

```text
Press 4 for deletion a file
Please tell your response :- 4

Enter which file you want to delete:- demo.txt
REMOVE SUCCESSFULLY
```

---

# 🔐 Safety and Data Considerations

This program performs real filesystem changes.

- **Overwrite** replaces existing file contents.
- **Delete** removes the selected file.
- Operations are intended for the `Files-Folders` workspace.
- The program does not provide backup, undo, or version history.

Use disposable test files when experimenting with overwrite and delete operations.

---

# ⚠️ Current Implementation Notes

The following points are documented from the current `main.py` implementation:

### 1. The menu is single-run
The program performs one selected top-level operation and then reaches the end of the script. A continuous menu loop is not currently implemented.

### 2. Input validation is basic
Top-level and update-menu selections are converted with `int(input(...))`. Non-numeric input can raise `ValueError`.

### 3. Some `exists` checks need correction
Several conditions use the method reference rather than calling the method, for example:

```python
if p.exists and p.is_file():
```

and:

```python
if not newP.exists:
```

These would normally be written using `exists()`.

### 4. Some exception messages do not interpolate `err`
The current code contains strings such as:

```python
print("An error occured as {err}")
```

Because the string is not an f-string, `{err}` is printed literally instead of displaying the exception value.

### 5. Naming and spelling can be improved
Examples include `breakPrg`, `dosen't`, `responce`, and `overwritr`. These do not prevent the core demonstration but can be cleaned up.

### 6. Scope is primarily text-file handling
The code demonstrates normal text read/write behavior and does not implement special processing for binary files such as images, PDFs, or videos.

---

# 🚀 Future Improvements

- Add a `while` loop for repeated operations in one execution.
- Improve numeric and filename validation.
- Catch specific filesystem exceptions instead of only broad exceptions.
- Correct `exists` method calls.
- Improve console wording and spelling.
- Add confirmation before overwrite and delete.
- Add copy and move functionality.
- Add directory creation and management.
- Add file search and metadata display.
- Add file extension filtering.
- Add unit tests for each operation.
- Add structured logging.
- Add stricter path validation.
- Add a GUI using Tkinter.

---

# 📝 Detailed Project Report

## 1. Introduction

File handling is a fundamental programming concept because applications frequently need to store, retrieve, modify, and remove information from the filesystem.

Python provides built-in facilities for filesystem operations. This project applies those concepts in a small command-line application so that learners can understand them through direct interaction.

## 2. Problem Statement

Beginners often learn file functions individually but may not understand how creation, reading, updating, and deletion fit into a complete workflow.

This project addresses that learning gap by combining common file operations into a single menu-driven program.

## 3. Proposed Solution

The proposed solution is a Python CLI utility centered around the `Files-Folders` workspace. The user chooses an operation, the relevant function constructs the target path, performs the requested action, and reports the result.

## 4. Scope

### In Scope
- File and directory listing
- File creation
- File reading
- File renaming
- File overwrite
- File append
- File deletion
- Basic exception handling
- Command-line interaction

### Out of Scope
- Database management
- Cloud storage
- Remote filesystem access
- Authentication
- Multi-user concurrency
- File versioning
- Encryption
- GUI
- Advanced file-type processing

## 5. Inputs

- Main menu choice
- File name
- Initial file content
- Replacement content
- Appended content
- New name during rename
- Rename confirmation when needed

## 6. Outputs

- Recursive workspace listing
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
  ▼
Select Operation
  │
  ├── Create ───────► Build Path ─► Write File
  │
  ├── Read ─────────► Build Path ─► Read File
  │
  ├── Update ───────► Choose Rename / Overwrite / Append
  │
  └── Delete ───────► Build Path ─► Remove File
  │
  ▼
Console Result
```

## 8. Module-Level Design

Although all application logic is inside one source file, its responsibilities can be viewed as:

```text
main.py
│
├── Program Control
│   └── breakPrg()
│
├── Workspace Inspection
│   └── readFileAndFolder()
│
├── Creation
│   └── createFile()
│
├── Reading
│   └── readFile()
│
├── Updating
│   ├── updateFile()
│   ├── renameFile()
│   ├── overwriteFile()
│   └── appendFile()
│
└── Deletion
    └── deleteFile()
```

## 9. Error Handling

Several functions use `try-except` to capture runtime failures. A future version can provide more precise handling for exceptions such as `FileNotFoundError`, `PermissionError`, `IsADirectoryError`, `NotADirectoryError`, and `ValueError`.

## 10. Benefits

- Simple for beginners to understand.
- Demonstrates multiple file operations in one project.
- Uses only Python's standard library.
- Gives practical experience with filesystem paths.
- Provides a foundation for a larger file-management application.

## 11. Limitations

The current version is primarily educational. It does not provide authentication, backups, undo, logging, advanced input validation, persistent application state, or production-grade filesystem protections.

## 12. Conclusion

The **Python File Handling** project provides a practical introduction to local filesystem programming in Python. By combining listing, creation, reading, updating, renaming, overwriting, appending, and deletion into one CLI application, it demonstrates how core Python file APIs can be integrated into a useful workflow.

The project also provides a clear foundation for future enhancements such as continuous navigation, safer input handling, automated testing, metadata support, and a graphical interface.

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