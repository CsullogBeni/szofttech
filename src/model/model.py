# TODO: Create run_program(command: str) method that executes the given command.
# TODO: Creat clear_history() method that clears the history.

# TODO: Create save_config(runnable: FileInfo, args: List) method that saves the given runnable and its arguments.
# TODO: Create load_config(runnable: FileInfo) method that loads the given runnable.
# TODO: Create __filter_main_runnables() method that filters the runnables that are marked as main.
# TODO: Create set_runnable_main_property(runnable: FileInfo, currently_mian: Bool) method that sets the main property of the given runnable.

# TODO: Create search_runnables(given_string: str) method that searches the given_string in __runnables and __main_runnables.
# TODO: Implement the searching algorithm in __searching_algorithm(given_string: str, runnables: List).

import sys
from typing import List
from queue import Queue
from os import path, listdir

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

    def __init__(self, working_directory_path: str, runnables: List[FileInfo], data_access: DataAccess):
        self.__working_directory_path = working_directory_path
        self.__runnables = runnables
        self.__data_access = data_access

    @property
    def get_working_directory_path(self):
        """
        Getter for the working directory path.

        Returns:
            str: the path to the current working directory.
        """
        return self.__working_directory_path

    @property
    def get_runnables(self):
        """
        Getter the list of runnables.

        Returns:
            str: the list of runnables.
        """
        return self.__runnables

    @property
    def get_data_access(self):
        """
        Getter the data accessor.

        Returns:
            str: the data accessor.
        """
        return self.__data_access

    def add_default_path(self):
        """
        Appends the current working directory using sys.path.
        """
        sys.path.append(self.__working_directory_path)

    def add_working_directory_path(self, workdir: str):
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
