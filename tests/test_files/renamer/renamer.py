import argparse
import os


def rename_file_or_directory(full_path: str, new_name: str, overwrite: bool = False, file: str = 'file') -> None:
    """
    Decides whether a file or directory will be renamed and calls the appropriate functions.

    Args:
        full_path (str): The full path to the file or directory to be renamed.
        new_name (str): The new name for the file or directory.
        overwrite (bool, optional): Whether to overwrite the existing file or not. Defaults to False.
        file (str, optional): Whether the path is a file or directory. Defaults to 'file'.

    Raises:
        FileNotFoundError: If the file or directory is not found.
        ValueError: If the new name is the same as the old name or if the new name contains '.' for a directory.
        IOError: If the path is not a file or directory.
        FileExistsError: If the file or directory already exists.
    """
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"File or directory not found: {full_path}")

    directory = os.path.dirname(full_path)
    if os.path.join(directory, new_name) == full_path:
        raise ValueError(f"New name is the same as the old name: {full_path}")

    if file == 'file':
        _rename_file(full_path, new_name, directory, overwrite)
    elif file == 'directory':
        _rename_directory(full_path, new_name, directory, overwrite)
    else:
        raise ValueError(f"Invalid file type: {file}")


def _rename_file(full_path: str, new_name: str, directory: str, overwrite: bool = False) -> None:
    """
    Renames a file.

    Args:
        full_path (str): The full path to the file to be renamed.
        new_name (str): The new name for the file.
        directory (str): The directory of the file to be renamed.
        overwrite (bool, optional): Whether to overwrite the existing file or not. Defaults to False.

    Raises:
        IOError: If the path is not a file.
        FileExistsError: If the file already exists.
    """
    if not os.path.isfile(full_path):
        raise IOError(f"Path is not a file: {full_path}")
    if overwrite:
        if os.path.exists(os.path.join(directory, new_name)):
            os.remove(os.path.join(directory, new_name))
    else:
        if os.path.exists(os.path.join(directory, new_name)):
            raise FileExistsError(f"File already exists: {os.path.join(directory, new_name)}")
    os.rename(full_path, os.path.join(directory, new_name))


def _rename_directory(full_path: str, new_name: str, directory: str, overwrite: bool = False) -> None:
    """
    Renames a directory.

    Args:
        full_path (str): The full path to the directory to be renamed.
        new_name (str): The new name for the directory.
        directory (str): The directory of the file to be renamed.
        overwrite (bool, optional): Whether to overwrite the existing directory or not. Defaults to False.

    Raises:
        IOError: If the path is not a directory.
        ValueError: If the new name contains '.'.
        FileExistsError: If the directory already exists.
    """
    if not os.path.isdir(full_path):
        raise IOError(f"Path is not a directory: {full_path}")
    if '.' in new_name:
        raise ValueError(f"New name cannot contain '.': {new_name}")
    if overwrite:
        if os.path.exists(os.path.join(directory, new_name)):
            os.remove(os.path.join(directory, new_name))
    else:
        if os.path.exists(os.path.join(os.path.dirname(full_path), new_name)):
            raise FileExistsError(f"Directory already exists: {os.path.join(os.path.dirname(full_path), new_name)}")
    os.rename(full_path, os.path.join(directory, new_name))


def parse_arguments() -> argparse.Namespace:
    """
    Parse the command line arguments and return them.

    Returns:
        argparse.Namespace: The parsed arguments
    """
    parser = argparse.ArgumentParser()
    parser.prog = "Renamer"
    parser.description = ("This program can rename a file or directory. The new name is given from the user as the "
                          "command line arguments. The full path argument is required, it will be renamed.")
    parser.add_argument("--full_path", "-p", type=str, help="Full path to the file or directory to be renamed",
                        required=True)
    parser.add_argument("--new_name", "-n", type=str, help="New name for the file or directory", required=True)
    parser.add_argument("--overwrite", "-o", action="store_true",
                        help="Whether to overwrite the existing file or not", default=False)
    parser.add_argument("--file", "-f", choices=["file", "directory"], help="Whether the path is a file or not",
                        default='file', type=str)

    return parser.parse_args()


def main() -> None:
    """
    The main entry point of the file renamer.

    This function parses the command line arguments, renames the given file or directory
    and prints out the result.
    """
    args = parse_arguments()
    try:
        rename_file_or_directory(args.full_path, args.new_name, args.overwrite, args.file)
        print("Renaming successful.")
        print("New path:", os.path.join(os.path.dirname(args.full_path), args.new_name))
    except Exception as e:
        print(f"Error: {e}")
        print("Renaming failed.")


if __name__ == "__main__":
    main()
