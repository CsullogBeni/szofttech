# TODO: Create add_working_directory_path() method that adds the given path to current working directory and runs through the directory recursively, searching for runnables, consider using argument_visitor.
# TODO: Create add_default_path() method that ads the current working directory to default paths.
# TODO: Create run_program(command: str) method that executes the given command.
# TODO: Creat clear_history() method that clears the history.

# TODO: Create save_config(runnable: FileInfo, args: List) method that saves the given runnable and its arguments.
# TODO: Create load_config(runnable: FileInfo) method that loads the given runnable.
# TODO: Create __filter_main_runnables() method that filters the runnables that are marked as main.
# TODO: Create set_runnable_main_property(runnable: FileInfo, currently_mian: Bool) method that sets the main property of the given runnable.

# TODO: Create search_runnables(given_string: str) method that searches the given_string in __runnables and __main_runnables.
# TODO: Implement the searching algorithm in __searching_algorithm(given_string: str, runnables: List).

from typing import List
from model.fileinfo import FileInfo
from persistence.data_access import DataAccess
from model.argument import Argument
from queue import Queue
from os import path, listdir
from model.argument_visitor import extract_arguments

class Model:
    """
    Contains all the data about a runnable.

    Attributes:
    - __working_directory_path:  The path to the working directory
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
    def get_data_acces(self):
        """
        Getter the data accessor.

        Returns:
            str: the data accessor.
        """
        return self.__data_acces

    def add_working_directory_path(self, workdir: str):
        self.__working_directory_path = workdir
        self.__runnables = []
        queue = Queue()
        queue.put(self.__working_directory_path)
        while not (queue.empty()):
            elem = queue.get()
            if path.isdir(elem):
                for l in listdir(elem):
                    queue.put(path.join(elem, l))
            if path.isfile(elem):
                [nam, desc, args] = extract_arguments(elem)
                if nam == None or desc == None: continue
                # TODO: Figure out what actually "is main runnable" means
                self.__runnables.append(FileInfo(elem, nam, desc, [Argument(*arg) for arg in args], True))
