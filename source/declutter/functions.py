import logging
import shutil
from pathlib import Path
from declutter.extensions import formats

# Setup logging
log_folder = Path.cwd() / "logs_declutter.log"
log_format = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(filename=log_folder, level=logging.DEBUG, format=log_format)
logger = logging.getLogger(__name__)

def create(dest):
    """Create Declutter Directory and its Sub-directories."""
    try:
        dest_path = Path(dest)
        if not dest_path.exists():
            dest_path.mkdir(parents=True)
        
        logger.info(f"Creating DeClutter directory at {dest_path}")
        for category in formats.keys():
            cat_path = dest_path / category
            if not cat_path.exists():
                logger.info(f"Creating {category} directory")
                cat_path.mkdir()
        return True
    except Exception as e:
        logger.error(f"Error creating directories: {e}")
        return False

def get_unique_path(file_path):
    """Generate a unique filename if the file already exists."""
    if not file_path.exists():
        return file_path
    
    parent = file_path.parent
    stem = file_path.stem
    suffix = file_path.suffix
    counter = 1
    
    while True:
        new_path = parent / f"{stem}_{counter}{suffix}"
        if not new_path.exists():
            return new_path
        counter += 1

def organize(src, dest):
    """Move files into appropriate folders based on their extensions."""
    try:
        src_path = Path(src)
        dest_path = Path(dest)
        
        logger.info(f"Scanning files in {src_path}")
        
        # Filter files only (exclude directories and the destination directory itself)
        files = [f for f in src_path.iterdir() if f.is_file()]
        
        for file in files:
            file_type = file.suffix[1:].lower()
            target_category = None
            
            for category, extensions in formats.items():
                if file_type in extensions:
                    target_category = category
                    break
            
            if target_category:
                target_dir = dest_path / target_category
                target_path = target_dir / file.name
                
                if target_path.exists():
                    target_path = get_unique_path(target_path)
                    logger.warning(f"File exists. Renaming to {target_path.name}")
                
                logger.info(f"Moving {file.name} to {target_category}")
                shutil.move(str(file), str(target_path))
                
        return True
    except Exception as e:
        logger.error(f"Error during organization: {e}")
        return False

def remove(src, dest):
    """Move all files back to the source folder and delete Declutter structure."""
    try:
        src_path = Path(src)
        dest_path = Path(dest)
        
        if not dest_path.exists():
            return False

        logger.info(f"Moving files from {dest_path} back to {src_path}")
        
        for category_dir in dest_path.iterdir():
            if category_dir.is_dir():
                for file in category_dir.iterdir():
                    if file.is_file():
                        target_path = src_path / file.name
                        if target_path.exists():
                            target_path = get_unique_path(target_path)
                        
                        logger.info(f"Restoring {file.name}")
                        shutil.move(str(file), str(target_path))
                
                # Try to remove the category directory if empty
                try:
                    category_dir.rmdir()
                except OSError:
                    logger.warning(f"Could not remove non-empty directory: {category_dir}")
        
        # Finally remove the main dest directory
        try:
            dest_path.rmdir()
        except OSError:
            logger.warning(f"Could not remove main destination directory: {dest_path}")
            
        return True
    except Exception as e:
        logger.error(f"Error during removal: {e}")
        return False
