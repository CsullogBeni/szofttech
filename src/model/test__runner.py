import os
import argparse

from src.model.fileinfo import FileInfo
from src.model.model import Model

def main() -> None:
    args = parse_args()

    if args.path:
        if not os.path.isdir(args.path):
            raise AttributeError(f"Invalid path: {args.path}")

    run_tests(args.path)

def run_tests(path: str) -> None:
    model = Model()
    model.add_working_directory_path(path)
    for runnable in model.get_runnables:
        execute_test(runnable, model)