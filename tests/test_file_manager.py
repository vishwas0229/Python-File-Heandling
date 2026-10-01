import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import file_manager


class FileManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.old_workspace = file_manager.WORKSPACE
        file_manager.WORKSPACE = Path(self.temp_dir.name)

    def tearDown(self):
        file_manager.WORKSPACE = self.old_workspace
        self.temp_dir.cleanup()

    def test_create_read_overwrite_append(self):
        file_manager.create_file("docs/test.txt", "hello")
        self.assertEqual(file_manager.read_file("docs/test.txt"), "hello")

        file_manager.overwrite_file("docs/test.txt", "new")
        self.assertEqual(file_manager.read_file("docs/test.txt"), "new")

        file_manager.append_file("docs/test.txt", "!")
        self.assertEqual(file_manager.read_file("docs/test.txt"), "new!")

    def test_rename_requires_explicit_overwrite(self):
        file_manager.create_file("a.txt", "A")
        file_manager.create_file("b.txt", "B")

        with self.assertRaises(FileExistsError):
            file_manager.rename_file("a.txt", "b.txt")

        file_manager.rename_file("a.txt", "b.txt", overwrite=True)
        self.assertFalse((file_manager.WORKSPACE / "a.txt").exists())
        self.assertEqual(file_manager.read_file("b.txt"), "A")

    def test_delete_file_and_folder(self):
        file_manager.create_file("folder/a.txt", "data")
        file_manager.delete_file("folder/a.txt")
        self.assertFalse((file_manager.WORKSPACE / "folder/a.txt").exists())

        file_manager.create_file("folder/b.txt", "data")
        file_manager.delete_folder("folder")
        self.assertFalse((file_manager.WORKSPACE / "folder").exists())

    def test_path_traversal_is_rejected(self):
        with self.assertRaises(ValueError):
            file_manager.create_file("../outside.txt", "blocked")

        with self.assertRaises(ValueError):
            file_manager.read_file("/tmp/outside.txt")

    def test_copy_and_move(self):
        file_manager.create_file("source.txt", "data")
        file_manager.copy_item("source.txt", "copy.txt")
        self.assertEqual(file_manager.read_file("copy.txt"), "data")

        file_manager.move_item("copy.txt", "moved.txt")
        self.assertEqual(file_manager.read_file("moved.txt"), "data")

    def test_search_by_filename_pattern(self):
        file_manager.create_file("one.txt", "1")
        file_manager.create_file("nested/two.txt", "2")
        file_manager.create_file("nested/three.md", "3")

        results = file_manager.search_items("*.txt")
        self.assertEqual({p.name for p in results}, {"one.txt", "two.txt"})

    def test_metadata(self):
        file_manager.create_file("meta.txt", "123")
        metadata = file_manager.get_metadata("meta.txt")

        self.assertEqual(metadata["name"], "meta.txt")
        self.assertEqual(metadata["type"], "File")
        self.assertEqual(metadata["size"], 3)
        self.assertEqual(metadata["extension"], ".txt")

    @patch("builtins.input", side_effect=["abc", "0"])
    def test_menu_rejects_non_numeric_input(self, _mock_input):
        from main import prompt_choice

        with patch("builtins.print"):
            self.assertEqual(prompt_choice("Choice: ", {0}), 0)


if __name__ == "__main__":
    unittest.main()
