import logging
import re
import shutil
from pathlib import Path

from declutter.extensions import formats

# Creating a Logger for logs
log_folder = Path.cwd() / "logs_declutter.log"
log_format = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(filename=log_folder, level=logging.DEBUG, format=log_format)
logger = logging.getLogger()


# Create Declutter Directory and its Sub-directories
def create(dest="."):
    try:
        if not Path.exists(dest):
            Path.mkdir(dest)
        logger.info("Creating DeClutter directory")
        for extn in formats.keys():
            logger.info("Creating {} directory".format(extn))
            Path.mkdir(dest / extn)
        return True
    except Exception as e:
        return False


# Get File Extentions
def getFileType(path):
    return path.split(".")[-1]


# Rename files to avoid duplicate files
def rename(file, path="."):
    while Path.exists(path / file.name):
        i = 0
        temp = file.name
        newfilename = temp
        while True and i < 10:
            filename = temp.suffix
            number = re.findall("([0-9]+)$", filename[0])
            newfilename = filename[0]
            if not number:
                i += 1
            else:
                i = int(number[0]) + 1
                newfilename = re.sub("([0-9]+)$", "", filename[0])
            newfilename = newfilename + str(i) + filename[1]
            if Path.exists(Path.parent(file) / newfilename):
                i += 1
                temp = newfilename
            else:
                Path.rename(file, Path.parent(file) / newfilename)
                break
        file = Path.parent(file) / newfilename
    yield file


# Move files into appropriate folders
def organize(src=".", dest="."):
    try:
        logger.info("Getting file paths")
        paths = (Path(src / _) for _ in Path.iterdir(src) if not Path.is_dir(_))
        for path in paths:
            if path != __file__:
                fileType = path.suffix[1:]
                for types in formats:
                    if fileType in formats[types]:
                        logger.info(f"Moving {path.name} to {types} directory")
                        if Path.exists(dest / types / path.name):
                            path = rename(Path.absolute(path), dest / types)
                            logger.warning(
                                f"File already exists in {dest / types}. Renaming file to {path.name}"
                            )
                        shutil.move(path, dest / types)
        return True
    except Exception as e:
        logger.error("Exception caught {}".format(e))
        return False


# Move all files in the main folder and delete Declutter
def remove(src=".", dest="."):
    try:
        logger.info("Moving all files to {}".format(src))
        paths = [folders for folders in Path.iterdir(dest)]
        for path in paths[::-1]:
            for file in Path.iterdir(path):
                logger.info("Moving {}".format(file.name))
                shutil.move(path / file, src)
            Path.rmdir(path)
        logger.info("Removing DeClutter")
        Path.rmdir(dest)
        return True
    except Exception as e:
        logger.error("Exception caught {}".format(e))
        return False
