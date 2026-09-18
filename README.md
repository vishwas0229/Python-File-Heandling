# 🐍 Python File Handling

> A beginner-friendly, menu-driven Python CLI application for learning and practicing file and folder management using the standard library.

## 📌 Project Overview

**Python File Handling** is a command-line application that demonstrates practical filesystem operations inside a dedicated `Files-Folders` workspace.

The current implementation supports:

- 📂 Recursive file and folder listing
- 📝 File creation with initial content
- 📖 Text-file reading
- ✏️ File update operations
- 🔄 File renaming
- 🧹 File overwrite with confirmation
- ➕ File content append
- 🗑️ File deletion
- 📁 Folder deletion
- 📋 File/folder metadata display
- 🔎 File/folder name search
- 📄 File copying
- 🚚 File/folder moving
- 🛡️ Basic path-traversal protection
- 🔢 Continuous menu navigation
- 🚪 Safe program exit

The project is implemented in a single **`main.py`** file and uses Python's standard library. No third-party Python packages are required.

---

# 🎯 Objectives

The project demonstrates:

1. Creating and managing filesystem paths with `pathlib.Path`.
2. Reading, writing, overwriting, and appending text files.
3. Renaming, copying, moving, and deleting filesystem items.
4. Recursively listing and searching files and folders.
5. Inspecting basic filesystem metadata.
6. Validating command-line input.
7. Protecting operations inside a defined workspace.
8. Using `try-except` for filesystem errors.
9. Building a reusable menu-driven CLI workflow.

---

# ✨ Features

## 📂 1. List Files and Folders

`readFileAndFolder()` recursively scans `Files-Folders/` using `rglob("*")` and displays each item with a **FILE** or **DIR** indicator.

## 📝 2. Create a File

The program asks for a target name and initial content. Parent directories are created when required.

## 📖 3. Read a File

Existing files are read as UTF-8 text and displayed in the terminal.

## ✏️ 4. Update a File

The update menu provides:

| Option | Operation | Description |
|---:|---|---|
| 1 | Rename | Change the file name |
| 2 | Overwrite | Replace all existing content |
| 3 | Append | Add new content to the file |

## 🔄 5. Rename

Renaming uses `Path.rename()`. If the destination already exists, the user is asked whether it should be overwritten.

## 🧹 6. Overwrite

The application asks for confirmation before replacing file content.

## ➕ 7. Append

New text is added using append mode without automatically inserting an extra space.

## 🗑️ 8. Delete File or Folder

The delete menu distinguishes between files and folders and requires confirmation before deletion.

- Files are removed with `Path.unlink()`.
- Folders are removed recursively with `shutil.rmtree()`.

## 📋 9. File/Folder Metadata

`showMetadata()` displays:

- Path
- Type
- Size in bytes
- Last modified timestamp
- Permission bits

## 🔎 10. Search

`searchFiles()` searches recursively by matching the supplied text against file and folder names.

## 📄 11. Copy

`copyFile()` copies a file with metadata using `shutil.copy2()`.

## 🚚 12. Move

`moveFile()` moves a file or folder with `shutil.move()`.

## 🛡️ 13. Workspace Path Protection

`get_target()` resolves the requested path and rejects paths that escape the `Files-Folders` workspace. This helps prevent accidental operations outside the project workspace.

## 🔢 14. Input Validation and Continuous Menu

`get_menu_choice()` validates numeric menu selections, while `main()` keeps the application running until the user selects **0 - Exit**.

---

# 🧰 Technologies Used

| Technology / Module | Usage |
|---|---|
| **Python 3** | Core programming language |
| **pathlib** | Paths, traversal, file checks, metadata, renaming |
| **os** | Imported for filesystem compatibility/utilities |
| **shutil** | Copying, moving, and recursive folder deletion |
| **File I/O** | Reading, writing, overwriting, and appending |
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

The current application provides:

```text
========== PYTHON FILE HANDLING ==========
1. Create a file
2. Read a file
3. Update a file
4. Delete a file/folder
5. List files and folders
6. Copy a file
7. Move a file/folder
8. Search files and folders
9. Show file/folder metadata
0. Exit
```

### Update Menu

```text
Press 1 for rename
Press 2 for overwriting data
Press 3 for append data
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
       ┌──────────┬────────┼────────┬───────────┐
       ▼          ▼        ▼        ▼           ▼
     Create      Read    Update    Delete      Other
       │          │        │        │           │
       │          │     ┌──┼──┐     │      ┌────┼────┬────┐
       │          │     │  │  │     │      │    │    │    │
       │          │   Rename │ Append │    List Copy Move Search Metadata
       │          │      Overwrite   │
       └──────────┴────────┴────────┴───────────┘
                           │
                           ▼
                     Return to Menu
                           │
                     ┌─────┴─────┐
                     │  Exit (0) │
                     └───────────┘
```

---

# 🧩 Functions in `main.py`

| Function | Responsibility |
|---|---|
| `print_separator()` | Prints a visual separator |
| `ensure_workspace()` | Creates the workspace when needed |
| `get_target(name)` | Validates and resolves workspace paths |
| `readFileAndFolder()` | Recursively lists files and directories |
| `createFile()` | Creates a file and writes initial content |
| `readFile()` | Reads a UTF-8 text file |
| `renameFile(path)` | Renames a file |
| `overwriteFile(path)` | Replaces file contents |
| `appendFile(path)` | Appends new content |
| `updateFile()` | Selects rename, overwrite, or append |
| `deleteFile()` | Deletes a file or folder |
| `copyFile()` | Copies a file |
| `moveFile()` | Moves a file or folder |
| `searchFiles()` | Searches file/folder names |
| `showMetadata()` | Displays filesystem metadata |
| `get_menu_choice()` | Validates numeric menu input |
| `main()` | Runs the continuous CLI menu |

---

# 📚 File Handling Concepts Demonstrated

## File Modes

| Mode | Meaning | Project Usage |
|---|---|---|
| `r` | Read | Read file contents |
| `w` | Write/overwrite | Create or replace text |
| `a` | Append | Add text to an existing file |

The implementation also uses `Path.read_text()`, `Path.write_text()`, and `Path.open()` with UTF-8 encoding.

## Recursive Traversal

`Path.rglob("*")` discovers files and folders below the workspace.

## Path Management

`Path` objects are used instead of manually concatenating filesystem strings.

## File Operations

The project demonstrates:

```text
Create → Read → Update → Rename
                   │
                   ├── Overwrite
                   └── Append

Copy / Move / Delete / Search / Metadata
```

---

# 🏗️ Technical Architecture

The project follows a small procedural CLI architecture:

```text
                 USER
                   │
                   ▼
              main() / CLI
                   │
          ┌────────┼─────────┐
          ▼        ▼         ▼
      Validation  Operation  Workspace
          │        │         │
          │   ┌────┼────┐     │
          │   ▼    ▼    ▼     ▼
          │ Create Read Update Files-Folders/
          │             │
          │        ┌────┼────┐
          │      Rename Overwrite Append
          │
          └── Copy / Move / Delete / Search / Metadata
```

There is no database, web server, GUI, authentication system, external API, or third-party Python dependency.

---

# 📋 Functional Requirements

1. The system shall maintain a dedicated filesystem workspace.
2. The system shall list files and directories recursively.
3. The system shall create new text files.
4. The system shall read existing text files.
5. The system shall rename files.
6. The system shall overwrite file content after confirmation.
7. The system shall append file content.
8. The system shall delete files and folders after confirmation.
9. The system shall copy files.
10. The system shall move files and folders.
11. The system shall search file and folder names.
12. The system shall display basic file/folder metadata.
13. The system shall validate menu input.
14. The system shall reject paths outside the workspace.
15. The system shall continue running until the user selects Exit.

---

# ⚙️ Non-Functional Requirements

### Usability
The application uses simple numbered choices and confirmation prompts.

### Portability
It uses Python's standard library and does not require third-party packages.

### Maintainability
Operations are separated into dedicated functions.

### Safety
Overwrite and delete actions require confirmation, and target paths are constrained to the workspace.

### Simplicity
The project remains a single-file educational CLI so the filesystem concepts are easy to study.

---

# 🧪 Test Scenarios

| # | Scenario | Expected Result |
|---:|---|---|
| 1 | Create a new file | File is created with supplied content |
| 2 | Create an existing file | Existing-path message is shown |
| 3 | Read an existing text file | Content is displayed |
| 4 | Rename a file | File receives the new name |
| 5 | Overwrite a file and confirm | Existing content is replaced |
| 6 | Overwrite and decline | Content remains unchanged |
| 7 | Append content | New content is added |
| 8 | Delete a file and confirm | File is removed |
| 9 | Delete a folder and confirm | Folder and its contents are removed |
| 10 | Copy a file | Destination file is created |
| 11 | Move a file/folder | Source is moved to destination |
| 12 | Search by name | Matching paths are displayed |
| 13 | Show metadata | Path, type, size, timestamp, permissions are displayed |
| 14 | Enter invalid menu input | User is asked for a valid number |
| 15 | Enter `../outside` path | Path validation rejects the operation |
| 16 | Select `0` | Program exits cleanly |

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

### Create

```text
1. Create a file
Enter new file name:- notes.txt
What you want to write in that file:- Learning Python
FILE CREATED SUCCESSFULLY
```

### Read

```text
2. Read a file
Enter file name you want to read:- notes.txt
Learning Python
READ SUCCESSFULLY
```

### Update → Append

```text
3. Update a file
Enter file name you want to update:- notes.txt
Press 1 for rename
Press 2 for overwriting data
Press 3 for append data
Enter your response:- 3
Tell what you want to append:- is useful.
APPEND SUCCESSFULLY
```

### Copy / Move

```text
6. Copy a file
7. Move a file/folder
```

### Search / Metadata

```text
8. Search files and folders
9. Show file/folder metadata
```

---

# 🔐 Safety and Data Considerations

This application performs real filesystem changes.

- Overwrite permanently replaces current text content.
- Delete permanently removes the selected file or folder.
- Folder deletion is recursive.
- Copy and move operations change filesystem state.
- The application restricts targets to the `Files-Folders` workspace.
- There is no backup, undo, or version history.

Use disposable test data while learning.

---

# 📝 Current Implementation Status

The current `main.py` already includes the major improvements that were previously tracked as planned issues:

- ✅ Correct `Path.exists()` usage
- ✅ Better exception messages
- ✅ Numeric menu validation
- ✅ Continuous menu loop
- ✅ Confirmation for overwrite/delete
- ✅ Workspace path validation
- ✅ Copy operation
- ✅ Move operation
- ✅ Search functionality
- ✅ Metadata viewer
- ✅ Improved CLI messages and naming

Remaining project-level improvements can focus on automated tests and further modularization.

---

# 🚀 Future Improvements

- Add automated unit/integration tests.
- Refactor the single `main.py` file into modules.
- Add structured logging.
- Add richer file-content search.
- Add file extension/type filters.
- Add directory creation and dedicated directory management.
- Add timestamps in a more readable format.
- Add a GUI using Tkinter.
- Add optional configuration for the workspace path.
- Add backup/restore or undo functionality.

---

# 📝 Detailed Project Report

## 1. Introduction

File handling is a fundamental programming concept because software frequently needs to create, retrieve, modify, move, copy, and remove data stored on a filesystem.

This project turns those individual Python concepts into one interactive CLI application.

## 2. Problem Statement

Beginners may understand individual file functions but have difficulty connecting them into a complete filesystem workflow.

This project provides a practical learning environment where common file and folder operations can be performed through a single command-line interface.

## 3. Proposed Solution

The application uses `Files-Folders/` as a controlled workspace. User input is validated, converted into a safe `Path`, and passed to the appropriate operation.

The application continues to display its menu until the user chooses Exit.

## 4. Scope

### In Scope

- File/folder listing
- File creation
- File reading
- File renaming
- File overwrite
- File append
- File/folder deletion
- File copying
- File/folder moving
- Name-based search
- Metadata display
- Input validation
- Workspace path validation
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

- Main menu choice
- File/folder name
- Initial file content
- Replacement content
- Appended content
- New name during rename
- Source/destination paths
- Confirmation responses
- Search query

## 6. Outputs

- Workspace listing
- File contents
- Operation status messages
- Search results
- File/folder metadata
- Validation and error messages

## 7. Data Flow

```text
User
  │
  ▼
Main Menu
  │
  ├── Create ───► Validate Path ───► Write
  ├── Read ─────► Validate Path ───► Read
  ├── Update ───► Validate Path ───► Rename / Overwrite / Append
  ├── Delete ───► Validate Path ───► Confirm ───► Remove
  ├── Copy ─────► Validate Paths ──► Copy
  ├── Move ─────► Validate Paths ──► Move
  ├── Search ───► Recursive Scan ──► Results
  └── Metadata ─► Validate Path ───► stat()
  │
  ▼
Return to Menu
  │
  ▼
Exit
```

## 8. Error Handling

The application catches common filesystem and validation failures and reports the actual exception message.

Examples include invalid paths, missing files, permission problems, and invalid menu input.

## 9. Benefits

- Beginner-friendly.
- Practical demonstration of Python filesystem APIs.
- Uses only the standard library.
- Covers both file and folder operations.
- Includes basic safety protections.
- Provides a foundation for future testing and modularization.

## 10. Limitations

The current version remains an educational CLI application. It does not provide production-grade backup, authentication, audit logging, concurrent access control, undo/versioning, or advanced file-content indexing.

## 11. Conclusion

**Python File Handling** demonstrates how Python's filesystem APIs can be combined into a practical command-line workflow.

The current implementation has evolved beyond basic CRUD-style file handling and now includes continuous navigation, safer path handling, copy/move operations, search, metadata inspection, and confirmation prompts.

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
