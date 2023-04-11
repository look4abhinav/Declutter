from pathlib import Path

from declutter.functions import create, organize, remove

src_path = Path.cwd()
dest_path = src_path / "Declutter"

if __name__ == "__main__":
    print("Welcome to DeClutter")
    print("Source:      ", src_path)
    print("Destination: ", dest_path)

    if not Path.exists(dest_path):
        print("Running...")
        try:
            create(dest_path)
        except Exception as e:
            print(e)
        finally:
            organize(src_path, dest_path)
            print("Successful!")

    else:
        print("Removing Files...")
        organize(src_path, dest_path)
        remove(src_path, dest_path)
        print("Files removed successfully")
