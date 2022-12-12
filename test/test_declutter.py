from pathlib import Path
import random

from declutter.functions import create, organize, remove
from declutter.extensions import formats


def setup_files():
    cwd = Path.cwd()
    test_dir = cwd / "SampleFiles"
    for i in range(5):
        file = test_dir / random.choice(formats)
        print(file)


def test_create():
    assert create(Path.cwd())
    assert create(Path.cwd().parent)
    assert create(Path.cwd() / "Test")


def test_remove():
    pass


def test_organize():
    pass


if __name__ == "__main__":
    setup_files()
