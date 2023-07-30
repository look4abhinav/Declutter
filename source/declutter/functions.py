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
            logger.info(f"Creating {extn} directory")
            Path.mkdir(dest / extn)
        return True
    except Exception:
        return False


# Rename files to avoid duplicate files
def rename(file, path="."):
    while Path.exists(path / file.name):
        i = 0
        temp = file.name
        newfilename = temp
        while i < 10:
            filename = file.stem
            number = re.findall("([0-9]+)$", filename)
            newfilename = filename
            if not number:
                i += 1
            else:
                i = int(number[0]) + 1
                newfilename = re.sub("([0-9]+)$", "", filename)
            newfilename = newfilename + str(i) + file.suffix
            if Path.exists(file.parent / newfilename):
                i += 1
                temp = newfilename
            else:
                newname = Path.rename(file, file.parent / newfilename)
                break
    return newname


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
        logger.error(f"Exception caught {str(e)}")
        return False


# Move all files in the main folder and delete Declutter
def remove(src=".", dest="."):
    try:
        logger.info(f"Moving all files to {src}")
        paths = list(Path.iterdir(dest))
        for path in paths[::-1]:
            for file in Path.iterdir(path):
                logger.info(f"Moving {file.name}")
                shutil.move(path / file, src)
            Path.rmdir(path)
        logger.info("Removing DeClutter")
        Path.rmdir(dest)
        return True
    except Exception as e:
        logger.error(f"Exception caught {str(e)}")
        return False
