from pathlib import Path
import random
import unittest

from declutter.functions import create, organize, remove
from declutter.extensions import formats


class Testcases(unittest.TestCase):
    def setup_files(self):
        cwd = Path.cwd()
        test_dir = cwd / "SampleFiles"
        for file_type in formats:
            file = test_dir / formats[file_type][random.randint(0, 2)]
            print(file)

    def test_create(self):
        assert True

    def test_remove(self):
        assert True

    def test_organize(self):
        assert True


if __name__ == "__main__":
    unittest.main()
