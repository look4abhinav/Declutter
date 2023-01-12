import os
import random
import unittest
from pathlib import Path

from declutter.extensions import formats
from declutter.functions import create, organize, remove


class Testcases(unittest.TestCase):
    def setup_files(self, target):
        for file_type in formats:
            filename = (
                "file"
                + str(random.randint(0, 2))
                + "."
                + formats[file_type][random.randint(0, 2)]
            )
            file = target / filename
            os.system(f"touch {file}")

    def test_create(self):
        path = Path.cwd() / "Declutter"
        assert create(path)

    def test_remove(self):
        self.test_organize()
        assert remove()

    def test_organize(self):
        path = Path.cwd()
        src = path / "SampleFiles"
        dest = path / "Declutter"
        os.mkdir(dest)
        self.test_create()
        self.setup_files(src)
        assert organize(src, dest)


if __name__ == "__main__":
    # unittest.main()
    t = Testcases()
    t.test_create()
