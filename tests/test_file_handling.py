import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import main


class FileHandlingTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_base_dir = main.BASE_DIR
        main.BASE_DIR = Path(self.temp_dir.name)

    def tearDown(self):
        main.BASE_DIR = self.original_base_dir
        self.temp_dir.cleanup()

    def test_create_and_read_file(self):
        with patch("builtins.input", side_effect=["test.txt", "Hello Python"]):
            main.createFile()

        path = main.BASE_DIR / "test.txt"
        self.assertTrue(path.is_file())
        self.assertEqual(path.read_text(encoding="utf-8"), "Hello Python")

    def test_append_file(self):
        path = main.BASE_DIR / "test.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("Hello", encoding="utf-8")

        with patch("builtins.input", return_value=" World"):
            main.appendFile(path)

        self.assertEqual(path.read_text(encoding="utf-8"), "Hello World")

    def test_rename_file(self):
        path = main.BASE_DIR / "old.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("data", encoding="utf-8")

        with patch("builtins.input", return_value="new.txt"):
            main.renameFile(path)

        self.assertFalse(path.exists())
        self.assertTrue((main.BASE_DIR / "new.txt").is_file())

    def test_delete_file_requires_confirmation(self):
        path = main.BASE_DIR / "delete.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("data", encoding="utf-8")

        with patch("builtins.input", side_effect=["1", "delete.txt", "y"]):
            main.deleteFile()

        self.assertFalse(path.exists())

    def test_path_traversal_is_rejected(self):
        with self.assertRaises(ValueError):
            main.get_target("../outside.txt")


if __name__ == "__main__":
    unittest.main()
