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


