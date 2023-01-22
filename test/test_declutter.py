import os
import random
import unittest
from pathlib import Path

from declutter.extensions import formats
from declutter.functions import create, organize, remove


class Testcases(unittest.TestCase):
    def test_create(self):
        src = Path.cwd() / "test" / "DummyFiles"
        dest = src / "Declutter"
        assert create(dest)

    def test_organize(self):
        src = Path.cwd() / "test" / "DummyFiles"
        dest = src / "Declutter"
        assert organize(src, dest)

    def test_remove(self):
        src = Path.cwd() / "test" / "DummyFiles"
        dest = src / "Declutter"
        assert remove(src, dest)


if __name__ == "__main__":
    unittest.main()
