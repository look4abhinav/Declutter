import argparse
import sys
from pathlib import Path
from declutter.functions import create, organize, remove

def main():
    parser = argparse.ArgumentParser(description="Organize files in a directory by their extension.")
    parser.add_argument("source", nargs="?", default=".", help="Source directory to declutter (default: current directory)")
    parser.add_argument("--dest", default="Declutter", help="Destination folder name (default: Declutter)")
    parser.add_argument("--undo", action="store_true", help="Undo the decluttering process and move files back")

    args = parser.parse_args()

    src_path = Path(args.source).resolve()
    dest_path = src_path / args.dest

    print("Welcome to DeClutter")
    print(f"Source:      {src_path}")
    print(f"Destination: {dest_path}")

    if not src_path.is_dir():
        print(f"Error: {src_path} is not a valid directory.")
        sys.exit(1)

    if args.undo:
        if not dest_path.is_dir():
            print(f"Error: {dest_path} not found. Nothing to undo.")
            sys.exit(1)
        print("Undoing decluttering...")
        if remove(src_path, dest_path):
            print("Files moved back successfully.")
        else:
            print("Failed to undo decluttering.")
    else:
        if not dest_path.exists():
            print("Creating directory structure...")
            if not create(dest_path):
                print("Failed to create destination directory.")
                sys.exit(1)
        
        print("Organizing files...")
        if organize(src_path, dest_path):
            print("Decluttering successful!")
        else:
            print("Decluttering failed. Check logs for details.")

if __name__ == "__main__":
    main()
