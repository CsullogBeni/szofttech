# TODO: Creat clear_history() method that clears the history.

# TODO: Create __filter_main_runnables() method that filters the runnables that are marked as main.
# TODO: Create set_runnable_main_property(runnable: FileInfo, currently_mian: Bool) method that sets the main property of the given runnable.

# TODO: Create search_runnables(given_string: str) method that searches the given_string in __runnables and __main_runnables.
# TODO: Implement the searching algorithm in __searching_algorithm(given_string: str, runnables: List).

import sys
from typing import List, Tuple, Optional
from subprocess import CompletedProcess
from typing import List
from queue import Queue
from os import path, listdir
import subprocess

from src.persistence.data_access import DataAccess
from src.model.argument import Argument
from src.model.fileinfo import FileInfo
from src.model.argument_visitor import extract_arguments


class Model:
    """
    Contains all the data about a runnable.

    Attributes:
        __working_directory_path:  The path to the working directory
        __runnables:               The list of executables
        __data_access:             The data access object, handles IO operations
    """

    def __init__(self, working_directory_path: str, runnables: List[FileInfo], data_access: DataAccess) -> None:
        self.__working_directory_path = working_directory_path
        self.__runnables = runnables
        self.__data_access = data_access

    @property
    def get_working_directory_path(self) -> str:
        """
        Getter for the working directory path.

        Returns:
            str: the path to the current working directory.
        """
        return self.__working_directory_path

    @property
    def get_runnables(self) -> List[FileInfo]:
        """
        Getter the list of runnables.

        Returns:
            str: the list of runnables.
        """
        return self.__runnables

    @property
    def get_data_access(self) -> DataAccess:
        """
        Getter the data accessor.

        Returns:
            str: the data accessor.
        """
        return self.__data_access

    def add_default_path(self) -> None:
        """
        Appends the current working directory using sys.path.
        """
        sys.path.append(self.__working_directory_path)

    def add_working_directory_path(self, workdir: str) -> None:
        """
        Sets the working directory to the given path and recomputes the list of executables. Searches recursively.

        Args:
            workdir: The new working directory.
        """
        self.__working_directory_path = workdir
        self.__runnables = []
        queue = Queue()
        queue.put(self.__working_directory_path)
        while not (queue.empty()):
            elem = queue.get()
            if path.isdir(elem):
                [queue.put(path.join(elem, l)) for l in listdir(elem)]
            if path.isfile(elem):
                [nam, desc, args] = extract_arguments(elem)
                self.__runnables.append(FileInfo(elem, nam, desc, [Argument(*arg) for arg in args], False))

    # TODO: Add some concrete type for list
    # Educated guess: a parameter with a potential value
    def save_config(self, prog: FileInfo, args: List[Tuple[str, Optional[str]]]):
        """
        Saves a given program and its argument to JSON.

        Args:
            prog: The program.
            args: The arguments.
        """
        actual_args = prog.get_args
        args_to_keep = dict()
        for [a, v] in args:
            if any([a == p.get_id or a == p.get_second_id for p in actual_args]):
                args_to_keep[a] = v
            else:
                print(f"Model.save_config: Argument {a} couldn't be found in program {prog.get_prog_name}, skipping")
        self.__data_access.save_config(prog.get_prog_path, args_to_keep)

    # Will return list above for idempotency
    def load_config(self, prog: FileInfo) -> List[Tuple[str, Optional[str]]]:
        """
        Loads a given program's arguments from JSON.

        Args:
            prog: The program.
        """
        res_dict = self.__data_access.load_config(prog.get_prog_path)
        return [[k, v] for k, v in res_dict.items()]

    def save_main(self):
        """
        Dumps the list of main programs to JSON.
        """
        res = dict()
        # Bit confused why we're using json to store a list
        res['main'] = [p.get_prog_path for p in self.__runnables if p.get_is_main_runnable]
        self.__data_access.save_main_runnables(res)

    def load_main(self):
        """
        Loads the list of main programs from JSON.
        """
        mains = self.__data_access.load_main_runnables()['main']
        for idx, r in enumerate(self.__runnables):
            if r.get_prog_path in mains:
                self.__runnables[idx].set_main_runnable(True)

    def run_program(self, command: str) -> tuple[str, str] | tuple[None, str]:
        """
        This method executes the given command.

        Args:
            command: contains the full path of the executable and after it, its arguments

        Returns:
            tuple[str, str] | tuple[None, str]: the result of the executed command,
                first element of the tuple is from the stdout (it is None if there was an error), second is from stderr
        """
        try:
            result = subprocess.Popen(f"python {command}", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = result.communicate()
            return stdout.decode(), stderr.decode()
        except Exception as e:
            return None, str(e)
