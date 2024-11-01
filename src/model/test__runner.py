import os
import argparse

from src.model.fileinfo import FileInfo
from src.model.model import Model


def main() -> None:
    """
    The main entry point of the test runner.

    This function parses the command line arguments and calls the `run_tests` function
    with the given path.

    Args:
        None

    Returns:
        None
    """
    args = parse_args()

    if args.path:
        if not os.path.isdir(args.path):
            raise AttributeError(f"Invalid path: {args.path}")

    run_tests(args.path)


def run_tests(path: str) -> None:
    """
    Runs the tests in the given path.

    This function creates a new `Model`, adds the given path to its working directories,
    and then iterates over all its runnables. For each runnable, it calls the
    `execute_test` function.

    Args:
        path: The path to run the tests in

    Returns:
        None
    """
    model = Model()
    model.add_working_directory_path(path)
    for runnable in model.get_runnables:
        execute_test(runnable, model)


def execute_test(runnable: FileInfo, model: Model) -> None:
    if 'test_runner.py' in runnable.get_prog_path:
        return
    if 'test_' not in os.path.basename(runnable.get_prog_path):
        return
    out, err = model.run_program(runnable.get_prog_path)
    if out:
        print(out)
    else:
        print(err)


def parse_args() -> argparse.ArgumentParser.parse_args:
    parser = argparse.ArgumentParser()
    parser.prog = 'Test runner'
    parser.description = 'This tool runs the tests in the given folder.'
    parser.add_argument('-p', '--path', type=str, help='Path to the folder with tests', required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main()
