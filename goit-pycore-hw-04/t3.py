from pathlib import Path
from colorama import Fore, init
import sys
import os

def warning_log(error: str):
    print(f"{Fore.RED}{error}{Fore.RESET}")

def show_folder_content(path, space: int = 0):
    if len(sys.argv) != 2:
        warning_log('Arguments are written incorrectly')
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        warning_log('Path does not exist')
        sys.exit(1)
    if not os.path.isdir(sys.argv[1]):
        warning_log('Path is not a directory')
        sys.exit(1)
    try:
        for path in path.iterdir():
            spaces = space * 4 * ' '
            entity_name = Path(path).name
            if path.is_dir():
                print(f"{spaces}{Fore.BLUE}{entity_name}/{Fore.RESET}")
                show_folder_content(path, space + 1)
            elif path.is_file():
                print(f"{spaces}{Fore.GREEN}{entity_name}/{Fore.RESET}")
            else:
                print(f"Unknown path or entity type")
                sys.exit(1)
    except Exception as error:
        print(error)
        return None

def main():
    orig_path = Path(sys.argv[1])
    show_folder_content(orig_path)

if __name__ == '__main__':
    init() 
    main()





