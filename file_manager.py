from __future__ import annotations

from datetime import datetime
from fnmatch import fnmatch
from pathlib import Path
import shutil
from typing import Dict, List

WORKSPACE = Path(__file__).resolve().parent / "Files-Folders"


class FileManagerError(Exception):
    """Base exception for expected file-manager errors."""


def _workspace_path(name: str, *, allow_root: bool = False) -> Path:
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Path cannot be empty.")

    candidate = Path(name.strip())
    if candidate.is_absolute():
        raise ValueError("Absolute paths are not allowed.")

    root = WORKSPACE.resolve()
    target = (root / candidate).resolve()

    try:
        target.relative_to(root)
    except ValueError as exc:
        raise ValueError("Path must stay inside the Files-Folders workspace.") from exc

    if target == root and not allow_root:
        raise ValueError("The workspace directory cannot be used for this operation.")

    return target


def _relative(path: Path) -> str:
    return str(path.resolve().relative_to(WORKSPACE.resolve()))


def list_items() -> List[Path]:
    WORKSPACE.mkdir(parents=True, exist_ok=True)
    return sorted(WORKSPACE.rglob("*"), key=lambda item: str(item).lower())


def create_file(name: str, content: str = "") -> Path:
    path = _workspace_path(name)
    if path.exists():
        raise FileExistsError(f"Path already exists: {_relative(path)}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def read_file(name: str) -> str:
    path = _workspace_path(name)
    if not path.exists():
        raise FileNotFoundError(f"File does not exist: {_relative(path)}")
    if not path.is_file():
        raise IsADirectoryError(f"Path is not a file: {_relative(path)}")
    return path.read_text(encoding="utf-8")


def rename_file(name: str, new_name: str, *, overwrite: bool = False) -> Path:
    source = _workspace_path(name)
    destination = _workspace_path(new_name)

    if not source.exists():
        raise FileNotFoundError(f"Source file does not exist: {_relative(source)}")
    if not source.is_file():
        raise IsADirectoryError(f"Source path is not a file: {_relative(source)}")
    if destination.exists() and not overwrite:
        raise FileExistsError(
            f"Destination already exists: {_relative(destination)}"
        )

    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and overwrite:
        destination.unlink()
    source.rename(destination)
    return destination


def overwrite_file(name: str, content: str) -> Path:
    path = _workspace_path(name)
    if not path.exists():
        raise FileNotFoundError(f"File does not exist: {_relative(path)}")
    if not path.is_file():
        raise IsADirectoryError(f"Path is not a file: {_relative(path)}")
    path.write_text(content, encoding="utf-8")
    return path


def append_file(name: str, content: str) -> Path:
    path = _workspace_path(name)
    if not path.exists():
        raise FileNotFoundError(f"File does not exist: {_relative(path)}")
    if not path.is_file():
        raise IsADirectoryError(f"Path is not a file: {_relative(path)}")
    with path.open("a", encoding="utf-8") as file:
        file.write(content)
    return path


def delete_file(name: str) -> Path:
    path = _workspace_path(name)
    if not path.exists():
        raise FileNotFoundError(f"File does not exist: {_relative(path)}")
    if not path.is_file():
        raise IsADirectoryError(f"Path is not a file: {_relative(path)}")
    path.unlink()
    return path


def delete_folder(name: str) -> Path:
    path = _workspace_path(name)
    if not path.exists():
        raise FileNotFoundError(f"Folder does not exist: {_relative(path)}")
    if not path.is_dir():
        raise NotADirectoryError(f"Path is not a folder: {_relative(path)}")
    shutil.rmtree(path)
    return path


def copy_item(source_name: str, destination_name: str, *, overwrite: bool = False) -> Path:
    source = _workspace_path(source_name)
    destination = _workspace_path(destination_name)

    if not source.exists():
        raise FileNotFoundError(f"Source does not exist: {_relative(source)}")
    if destination.exists() and not overwrite:
        raise FileExistsError(
            f"Destination already exists: {_relative(destination)}"
        )

    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and overwrite:
        if destination.is_dir():
            shutil.rmtree(destination)
        else:
            destination.unlink()

    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        shutil.copy2(source, destination)
    return destination


def move_item(source_name: str, destination_name: str, *, overwrite: bool = False) -> Path:
    source = _workspace_path(source_name)
    destination = _workspace_path(destination_name)

    if not source.exists():
        raise FileNotFoundError(f"Source does not exist: {_relative(source)}")
    if destination.exists() and not overwrite:
        raise FileExistsError(
            f"Destination already exists: {_relative(destination)}"
        )

    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and overwrite:
        if destination.is_dir():
            shutil.rmtree(destination)
        else:
            destination.unlink()

    shutil.move(str(source), str(destination))
    return destination


def search_items(pattern: str) -> List[Path]:
    if not isinstance(pattern, str) or not pattern.strip():
        raise ValueError("Search pattern cannot be empty.")

    normalized = pattern.strip()
    matches = []
    for path in list_items():
        relative = _relative(path)
        if fnmatch(path.name, normalized) or fnmatch(relative, normalized):
            matches.append(path)
    return matches


def get_metadata(name: str) -> Dict[str, str | int]:
    path = _workspace_path(name)
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {_relative(path)}")

    stat = path.stat()
    item_type = "Directory" if path.is_dir() else "File"
    extension = path.suffix if path.is_file() else ""
    return {
        "path": _relative(path),
        "name": path.name,
        "type": item_type,
        "size": stat.st_size,
        "extension": extension,
        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(
            sep=" ", timespec="seconds"
        ),
    }
