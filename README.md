# 🐍 Python File Handling

> A beginner-friendly, menu-driven Python project for performing common file and directory operations using Python's built-in `pathlib` and `os` modules.

## 📌 Project Overview

**Python File Handling** is a console-based file management program developed to demonstrate how Python can interact with files and folders programmatically.

The application uses a dedicated `Files-Folders` directory as its working area and provides an interactive menu for common file operations. Users can create files, read file contents, update existing files, rename files, append data, overwrite file contents, and delete files.

This project is especially useful for students and beginners who are learning **Python File Handling, Path Management, Exception Handling, and basic CRUD-style operations on files**.

---

## 🎯 Objectives

The main objectives of this project are:

1. Understand how Python creates and manages files.
2. Practice reading and writing text files.
3. Learn how to append and overwrite existing file data.
4. Understand file renaming and deletion operations.
5. Learn how to work with file paths using `pathlib`.
6. Practice basic error handling using `try-except` blocks.
7. Build a simple interactive command-line utility using Python.

---

## ✨ Features

### 📂 Directory Listing
Displays the files and directories available inside the `Files-Folders` workspace using recursive path discovery.

### 📝 Create File
Creates a new file inside the working directory and accepts user input for the initial file content.

### 📖 Read File
Reads the complete content of a selected file and displays it in the terminal.

### ✏️ Update File
The update module provides three operations:

- **Rename** – change the file name.
- **Overwrite** – replace the existing file content.
- **Append** – add new content at the end of the file.

### 🗑️ Delete File
Removes an existing file from the `Files-Folders` directory.

### 🖥️ Interactive Menu
The program uses a simple numeric menu so that users can select an operation from the terminal.

### ⚠️ Basic Exception Handling
File operations are wrapped in `try-except` blocks in multiple functions to handle runtime errors without immediately terminating the program.

---

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3** | Core programming language |
| **pathlib** | File and directory path handling |
| **os** | File deletion operation |
| **File I/O** | Reading, writing, appending and updating files |
| **Git & GitHub** | Source-code management and project hosting |

### External Dependencies

No third-party Python packages are required.

The project relies only on Python's standard library.

---

## 🗂️ Project Structure

```text
Python-File-Heandling/
│
├── Files-Folders/
│   ├── Test.txt
│   └── test/
│
├── main.py
├── README.md
└── LICENSE
```

### File Description

| File / Folder | Description |
|---|---|
| `Files-Folders/` | Working directory where file operations are performed |
| `main.py` | Main Python program containing the file-handling logic |
| `README.md` | Project documentation and technical report |
| `LICENSE` | MIT License information |

The repository currently contains a small demonstration workspace under `Files-Folders`; the exact contents can be changed during testing.

---

# 🔄 Program Workflow

The program follows a straightforward command-line workflow:

```text
                 ┌──────────────────────┐
                 │      Start Program   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Display Main Menu    │
                 └──────────┬───────────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
      Create File      Read File        Update File
          │                 │                 │
          │                 │        ┌────────┼─────────┐
          │                 │        ▼        ▼         ▼
          │                 │      Rename  Overwrite  Append
          │                 │        │        │         │
          └─────────────────┴────────┴────────┴─────────┘
                            │
                            ▼
                     Delete File
                            │
                            ▼
                      Program End
```

> Note: In the current implementation, the menu is presented once and the program exits after completing the selected operation. It is not currently implemented as a continuous loop.

---

# 📋 Main Menu

When `main.py` is executed, the program provides these choices:

```text
Press 1 for creating a file
Press 2 for reading a file
Press 3 for updating a file
Press 4 for deletion a file
Press 0 for exit
```

For the update operation, the program provides:

```text
Press 1 for rename
Press 2 for overwriting data
Press 3 for append data
```

---

# 🧩 Functional Modules

The main program is divided into small functions, each handling a specific responsibility.

## `breakPrg()`

Provides the exit branch for the menu. In the current implementation it simply returns control without performing additional processing.

## `readFileAndFolder()`

Uses:

```python
Path('Files-Folders').rglob('*')
```

to discover files and directories recursively and print their paths.

### Purpose

- Inspect the working directory.
- Display available files before performing operations.
- Demonstrate recursive path traversal.

---

## `createFile()`

Creates a new file under `Files-Folders`.

### Process

1. Display existing files and directories.
2. Ask the user for a file name.
3. Build the path using `Path`.
4. Check whether the target path already exists.
5. Open the file in write mode.
6. Accept text from the user.
7. Write the content to the file.

### Example

```text
Enter new file name:- notes.txt
What you want to write in that file:- Python file handling is useful.
FILE CREATED SUCCESSFULLY
```

---

## `readFile()`

Reads and displays the content of a selected file.

### Process

1. Ask for the file name.
2. Build the target path.
3. Verify that the path represents a file.
4. Open the file in read mode.
5. Read the complete content.
6. Print the content to the console.

---

## `renameFile(p)`

Renames an existing file using `Path.rename()`.

### Process

1. Ask for a new file name.
2. Build the destination path.
3. Check whether the destination exists.
4. Rename the original path.
5. If the destination already exists, ask the user whether to continue.

---

## `overwriteFile(p)`

Replaces the current content of a file.

The file is opened using write mode:

```python
open(p, "w")
```

Write mode truncates the previous content and stores the newly entered content.

### Important

This operation is destructive with respect to the previous contents of the selected file.

---

## `appendFile(p)`

Adds new content to the end of an existing file.

The file is opened using append mode:

```python
open(p, "a")
```

The current implementation inserts a space before the appended text.

---

## `updateFile()`

Acts as the controller for all update-related operations.

After the user selects a file, the function provides three choices:

| Option | Operation |
|---:|---|
| `1` | Rename file |
| `2` | Overwrite file content |
| `3` | Append file content |

It then calls the appropriate helper function.

---

## `deleteFile()`

Deletes a selected file using:

```python
os.remove(p)
```

The function first checks that the supplied path exists and points to a file.

---

# 🧠 Concepts Demonstrated

This project provides practical exposure to several important Python concepts.

## 1. File I/O

The project demonstrates the three fundamental text-file modes:

| Mode | Purpose |
|---|---|
| `r` | Read existing content |
| `w` | Write / overwrite content |
| `a` | Append content |

## 2. `pathlib`

`pathlib.Path` is used to construct and work with filesystem paths in a structured way.

Example:

```python
p = Path('Files-Folders') / name
```

## 3. Recursive Directory Traversal

`rglob('*')` is used to inspect items recursively under the working directory.

## 4. Conditional Logic

`if`, `elif`, and `else` statements control menu selections and file existence checks.

## 5. Exception Handling

Several file operations use:

```python
try:
    ...
except Exception as err:
    ...
```

to catch runtime errors.

## 6. Functions and Modular Programming

Each file operation is separated into its own function, improving readability and making the code easier to understand and extend.

---

# 🏗️ Technical Architecture

The application follows a simple procedural architecture:

```text
User
  │
  ▼
CLI Menu
  │
  ├── Create Module ───────► Files-Folders
  │
  ├── Read Module ─────────► Files-Folders
  │
  ├── Update Module
  │      ├── Rename ───────► Files-Folders
  │      ├── Overwrite ────► Files-Folders
  │      └── Append ───────► Files-Folders
  │
  └── Delete Module ───────► Files-Folders
```

There is no database, web server, GUI framework, or external API. The filesystem itself acts as the project's data store.

---

# 📊 Functional Requirements

The system should be able to:

- Display available filesystem items inside the project workspace.
- Create a new file.
- Store user-provided text in a new file.
- Read an existing file.
- Rename an existing file.
- Overwrite existing content.
- Append additional content.
- Delete an existing file.
- Report common runtime failures through console messages.

---

# 📌 Non-Functional Requirements

### Usability

The interface should be simple enough for a beginner to operate from a terminal.

### Maintainability

Functions are separated according to operation, making future refactoring easier.

### Portability

The program uses standard Python modules and does not require third-party packages.

### Simplicity

The implementation intentionally uses a small codebase to keep the core file-handling concepts easy to study.

---

# 🧪 Example Test Scenarios

| Test Case | Input / Action | Expected Result |
|---|---|---|
| Create file | Select `1`, enter a new file name | File is created and content is written |
| Duplicate create | Select `1`, use an existing path | Program reports that the file already exists |
| Read file | Select `2`, enter an existing file | File content is displayed |
| Rename | Select `3` → `1` | File name is changed |
| Overwrite | Select `3` → `2` | Previous content is replaced |
| Append | Select `3` → `3` | New content is added to the end |
| Delete | Delete an existing file | File is removed |
| Invalid menu input | Enter an unsupported option | Program prints `INVALID INPUT` |

---

# ▶️ How to Run

## Prerequisites

Install **Python 3.x** on your system.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

## Step 1 — Clone the Repository

```bash
git clone https://github.com/vishwas0229/Python-File-Heandling.git
```

## Step 2 — Enter the Project Directory

```bash
cd Python-File-Heandling
```

## Step 3 — Run the Program

```bash
python main.py
```

On systems where `python` maps to another interpreter, use:

```bash
python3 main.py
```

---

# 💡 Usage Example

### Create a file

```text
Press 1 for creating a file
Please tell your response :- 1
Enter new file name:- demo.txt
What you want to write in that file:- Hello Python
FILE CREATED SUCCESSFULLY
```

### Read the file

Run the program again and select `2`:

```text
Enter file name you want to read:- demo.txt
Hello Python
READ SUCCESSFULLY
```

### Update the file

Select `3`, then choose one of the update operations:

```text
Press 1 for rename
Press 2 for overwriting data
Press 3 for append data
```

### Delete the file

The current top-level menu displays the delete option as `4`; the corresponding implementation exists in `deleteFile()`.

---

# 🔐 Safety and Data Considerations

This project performs real filesystem operations inside the `Files-Folders` workspace. In particular:

- **Overwrite** permanently replaces the existing content of the selected file.
- **Delete** removes the selected file from the filesystem.
- User input is used to construct target paths, so testing should be performed only with files inside the intended project workspace.
- The application does not maintain backups or version history.

For learning purposes, use disposable test files while experimenting with overwrite and delete operations.

---

# ⚙️ Current Implementation Notes

The repository is intentionally educational and compact. The current implementation has a few behaviors worth knowing:

1. The main menu is executed once rather than inside a continuous loop.
2. The delete operation is implemented in `deleteFile()`, while the current top-level menu contains the corresponding option `4`; integrating that branch into the main selection logic would make the option directly usable from the menu.
3. Some path existence checks in the current code use method objects without calling them, for example `p.exists` instead of `p.exists()`. These conditions can be improved in a future refactor.
4. Error messages and some variable/function names contain minor spelling inconsistencies.
5. Input validation is basic; non-numeric menu input can raise a `ValueError` because the menu uses `int(input(...))`.

These are implementation-level observations based on the current `main.py` and can be addressed as the project evolves.

---

# 🚀 Possible Future Improvements

The project can be extended with:

- A continuous menu loop until the user selects Exit.
- Complete integration of the delete option in the main menu.
- Better input validation and handling of invalid numeric input.
- More precise exception handling (`FileNotFoundError`, `PermissionError`, etc.).
- Support for creating nested directories.
- Separate directory creation and deletion features.
- File metadata display such as size and modification time.
- File extension filtering.
- Copy and move operations.
- Search functionality.
- Multi-file operations.
- Logging of user actions.
- A graphical user interface using Tkinter or another framework.
- Unit tests for each file operation.
- Improved path validation to keep operations restricted to the intended workspace.

---

# 📚 Learning Outcomes

After studying and running this project, a learner should have practical familiarity with:

- Python file and directory handling.
- File modes: `r`, `w`, and `a`.
- `pathlib.Path` operations.
- Recursive file discovery with `rglob()`.
- Basic use of the `os` module.
- Function-based program organization.
- Conditional branching.
- Console input/output.
- Basic exception handling.
- The relationship between application logic and filesystem data.

---

# 📝 Project Report

## 1. Introduction

File handling is one of the fundamental capabilities of a programming language because applications frequently need to store, retrieve, modify, and remove data. Python provides a straightforward interface for filesystem operations through built-in modules such as `pathlib` and `os`.

This project demonstrates these concepts by implementing a small command-line file management application. Instead of using a database, the application works directly with files stored in a dedicated project directory.

## 2. Problem Statement

Beginners often learn Python file-handling functions individually but may not understand how those operations work together in a practical program. There is therefore a need for a small, easy-to-understand application that combines common file operations into one workflow.

The project addresses this learning problem by providing an interactive utility for creating, reading, updating, renaming, appending to, overwriting, and deleting files.

## 3. Proposed Solution

The proposed solution is a menu-driven Python application that accepts an operation from the user and executes the corresponding filesystem task within the `Files-Folders` directory.

The application separates responsibilities into dedicated functions. This structure allows each operation to be studied independently while still demonstrating how the components work together in one program.

## 4. System Scope

The current scope includes local text-file management within the project workspace.

### Included

- File creation
- File reading
- File renaming
- File content overwrite
- File content append
- File deletion
- Recursive listing of files and directories

### Not included

- Database storage
- User authentication
- Cloud storage
- Remote file management
- File encryption
- Concurrent multi-user access
- GUI-based interaction

## 5. Input and Output

### Inputs

The application accepts:

- Menu selections.
- File names.
- New file content.
- Replacement file content.
- Appended content.
- New names during rename.
- Confirmation input when a destination already exists during rename.

### Outputs

The application produces:

- File and directory listings.
- File contents.
- Success messages.
- Error messages.
- Invalid-input notifications.

## 6. Data Flow

```text
User Input
    │
    ▼
Menu Selection
    │
    ▼
Operation Function
    │
    ▼
Path Construction
    │
    ▼
Filesystem Check
    │
    ▼
Read / Write / Rename / Delete
    │
    ▼
Console Result
```

## 7. Error Handling Strategy

The project uses `try-except` blocks around several operations. This allows unexpected runtime problems to be reported to the user rather than always terminating without context.

Future versions can improve this strategy by catching specific exceptions and giving operation-specific guidance.

## 8. Benefits of the Project

- Simple enough for beginners.
- Demonstrates multiple file-handling concepts in one program.
- Uses only the Python standard library.
- Provides hands-on practice with filesystem paths.
- Easy to extend into a larger file-management application.

## 9. Limitations

The current version is intended primarily as a learning project. The application is not designed as a production-grade file manager and does not provide advanced validation, authentication, backups, logging, or a persistent application state.

The current menu flow is also single-run rather than continuously interactive, and some implementation details can be improved during future refactoring.

## 10. Conclusion

The **Python File Handling** project provides a practical introduction to filesystem programming in Python. By combining creation, reading, updating, renaming, appending, overwriting, listing, and deletion operations into one console application, it demonstrates how basic Python file APIs can be integrated into a useful workflow.

The project establishes a solid foundation for future enhancements such as automated testing, stronger validation, continuous menu navigation, metadata inspection, directory management, and a graphical interface.

---

# 👨‍💻 Author

**Vishwas**

GitHub: [@vishwas0229](https://github.com/vishwas0229)

Repository: [Python-File-Heandling](https://github.com/vishwas0229/Python-File-Heandling)

---

# 📄 License

This project is licensed under the **MIT License**. See the [`LICENSE`](LICENSE) file for details.

---

⭐ If you are learning Python, feel free to explore the code, run the examples, and extend the project with additional file-management features.
