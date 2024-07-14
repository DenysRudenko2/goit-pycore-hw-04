import sys
from colorama import Fore, Style
from pathlib import Path


def print_dir_tree(dir_path: str, indent=0):
    for path in Path(dir_path).iterdir():
        if path.is_dir():
            print(Fore.BLUE + ' ' * indent + path.name + '/')
            print_dir_tree(str(path), indent + 4)
        else:
            print(Fore.GREEN + ' ' * indent + path.name)


def main():
    if len(sys.argv) != 2:
        print("You didn't provide the correct number of arguments!")
        sys.exit(1)

    dir_input = sys.argv[1]
    dir_path = Path(dir_input)
    if not dir_path.exists():
        print(f"Directory {dir_input} does not exist")
        sys.exit(1)

    if not dir_path.is_dir():
        print(f"Path {dir_input} is not a directory")
        sys.exit(1)

    try:
        print_dir_tree(sys.argv[1])
        print(Style.RESET_ALL)
    except Exception as e:
        sys.stderr.write(f"Error: {e}")


if __name__ == '__main__':
    main()
