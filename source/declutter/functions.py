import logging
import os
import re
import shutil

from formats import extensions


# Creating a Logger for logs
log_folder = os.path.join(os.getcwd(), "logs_declutter.log")
log_format = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(filename=log_folder, level=logging.DEBUG, format=log_format)
logger = logging.getLogger()


# Create Declutter Directory and its Sub-directories
def create(dest="."):
    try:
        os.mkdir(dest)
        logger.info("Creating DeClutter directory")
        for extn in extensions.keys():
            logger.info("Creating {} directory".format(extn))
            os.mkdir(os.path.join(dest, extn))
        return True
    except Exception as e:
        return False


# Get File Extentions
def getFileType(path):
    # path = os.path.splitext(path)[-1]
    return path.split(".")[-1]


# Rename files to avoid duplicate files
def rename(file, path="."):
    while os.path.exists(os.path.join(path, os.path.basename(file))):
        i = 0
        temp = os.path.basename(file)
        newfilename = temp
        while True and i < 10:
            filename = os.path.splitext(temp)
            number = re.findall("([0-9]+)$", filename[0])
            newfilename = filename[0]
            if not number:
                i += 1
            else:
                i = int(number[0]) + 1
                newfilename = re.sub("([0-9]+)$", "", filename[0])
            newfilename = newfilename + str(i) + filename[1]
            if os.path.exists(os.path.join(os.path.dirname(file), newfilename)):
                i += 1
                temp = newfilename
            else:
                os.rename(file, os.path.join(os.path.dirname(file), newfilename))
                break
        file = os.path.join(os.path.dirname(file), newfilename)
    yield file


# Move files into appropriate folders
def organize(src=".", dest="."):
    try:
        logger.info("Getting file paths")
        paths = (os.path.join(src, _) for _ in os.listdir(src) if not os.path.isdir(_))
        for path in paths:
            if path != __file__:
                fileType = getFileType(path)
                for types in extensions.keys():
                    if fileType in extensions[types]:
                        logger.info(
                            "Moving {} to {} directory".format(
                                os.path.basename(path), types
                            )
                        )
                        if os.path.exists(
                            os.path.join(
                                os.path.join(dest, types), os.path.basename(path)
                            )
                        ):
                            path = rename(
                                os.path.abspath(path), os.path.join(dest, types)
                            )
                            logger.warning(
                                "File already exists in {}. Renaming file to {}".format(
                                    os.path.join(dest, types), os.path.basename(path)
                                )
                            )
                        shutil.move(path, os.path.join(dest, types))
        return True
    except Exception as e:
        logger.error("Exception caught {}".format(e))
        return False


# Move all files in the main folder and delete Declutter
def remove(src=".", dest="."):
    try:
        logger.info("Moving all files to {}".format(src))
        paths = [folders[0] for folders in os.walk(dest)]
        for path in paths[::-1]:
            for file in os.listdir(path):
                logger.info("Moving {}".format(os.path.basename(file)))
                shutil.move(os.path.join(path, file), src)
            os.rmdir(path)
        logger.info("Removing DeClutter")
        return True
    except Exception as e:
        logger.error("Exception caught {}".format(e))
        return False
