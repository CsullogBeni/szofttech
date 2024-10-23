# TODO: Create run_program(command: str) method that executes the given command.
# TODO: Creat clear_history() method that clears the history.
import json
# TODO: Create __filter_main_runnables() method that filters the runnables that are marked as main.
# TODO: Create set_runnable_main_property(runnable: FileInfo, currently_mian: Bool) method that sets the main property of the given runnable.

# TODO: Create search_runnables(given_string: str) method that searches the given_string in __runnables and __main_runnables.
# TODO: Implement the searching algorithm in __searching_algorithm(given_string: str, runnables: List).

import os
import sys
from idlelib.outwin import file_line_pats
from typing import List, Tuple, Optional, Any
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

    def __init__(self, working_directory_path: str, runnables: List[FileInfo], data_access: DataAccess) -> None:
        self.__working_directory_path = working_directory_path
        loaded_working_directory_path = self.load_working_directory_path()
        if loaded_working_directory_path is not None:
            self.__working_directory_path = loaded_working_directory_path

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

    def get_app_data_dir(self) -> str:
        """
        This function get the path of the App Data Directory on the current system. If it doesn't exist, it creates it.

        Returns:
            str: the full path of the App Data Directory
        """
        app_name = "SZOFTECH"  # I am not sure about it, but in DataAccess we used this
        if os.name == 'nt':
            app_data_dir = os.path.join(os.environ['LOCALAPPDATA'], app_name)
        else:
            app_data_dir = os.path.join(os.path.expanduser('~'), '.local', 'share', app_name)

        if not os.path.exists(app_data_dir):
            os.makedirs(app_data_dir)

        return app_data_dir

    def save_working_directory_path(self, full_path: str) -> None:
        """
        This function saves the given path as the Model's working directory path into a json file in App Data Directory

        Args:
            full_path: the path to save as the Model's working directory path

        """
        data_to_save = dict()
        data_to_save['working_directory_path'] = full_path

        file_path = os.path.join(self.get_app_data_dir(), 'working_dir_path.json')

        with open(file_path, 'w') as json_file:
            json.dump(data_to_save, json_file)

    def load_working_directory_path(self) -> str | None:
        """
        This function loads the Model's working directory path from working_dir_path.json file in App Data Directory

        Returns:
            str | None: the loaded path, if it has been saved previously, or None if it hasn't
        """
        file_path = os.path.join(self.get_app_data_dir(), 'working_dir_path.json')

        if not os.path.exists(file_path):
            return None

        with open(file_path, 'r') as json_file:
            file_data = json.load(json_file)

            return file_data['working_directory_path']
