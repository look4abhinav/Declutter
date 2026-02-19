import unittest
from pathlib import Path
import shutil
from declutter.functions import create, organize, remove

class TestDeclutter(unittest.TestCase):
    def setUp(self):
        # Create a temp test directory
        self.test_dir = Path.cwd() / "test_workspace"
        self.test_dir.mkdir(exist_ok=True)
        self.dest_dir = self.test_dir / "Declutter"
        
        # Create some dummy files
        (self.test_dir / "test.txt").write_text("dummy text")
        (self.test_dir / "image.jpg").write_text("dummy image")
        (self.test_dir / "music.mp3").write_text("dummy audio")

    def tearDown(self):
        # Clean up the test directory
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_full_cycle(self):
        # Test Create
        self.assertTrue(create(self.dest_dir))
        self.assertTrue(self.dest_dir.exists())
        self.assertTrue((self.dest_dir / "Text").exists())

        # Test Organize
        self.assertTrue(organize(self.test_dir, self.dest_dir))
        self.assertTrue((self.dest_dir / "Text" / "test.txt").exists())
        self.assertFalse((self.test_dir / "test.txt").exists())

        # Test Remove (Undo)
        self.assertTrue(remove(self.test_dir, self.dest_dir))
        self.assertTrue((self.test_dir / "test.txt").exists())
        self.assertFalse(self.dest_dir.exists())

if __name__ == "__main__":
    unittest.main()
