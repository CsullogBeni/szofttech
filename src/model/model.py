# TODO: Creat clear_history() method that clears the history.
# TODO: Create __filter_main_runnables() method that filters the runnables that are marked as main.
# TODO: Create set_runnable_main_property(runnable: FileInfo, currently_mian: Bool) method that sets the main property of the given runnable.

# TODO: Create search_runnables(given_string: str) method that searches the given_string in __runnables and __main_runnables.
# TODO: Implement the searching algorithm in __searching_algorithm(given_string: str, runnables: List).

import os
import pathlib
import subprocess
import sys
from typing import List
from typing import Tuple, Optional

from src.model.argument import Argument
from src.model.argument_visitor import extract_arguments
from src.model.fileinfo import FileInfo
from src.persistence.data_access import DataAccess


class Model:
    """
    Contains all the data about a runnable.

    Attributes:
        __working_directory_path:  The path to the working directory
        __runnables:               The list of executables
        __data_access:             The data access object, handles IO operations
    """

    def __init__(self, working_directory_path: str = None) -> None:
        self.__data_access = DataAccess()
        self.__runnables = []
        self.__working_directory_path = None
        if working_directory_path is not None:
            if os.path.isdir(working_directory_path):
                self.__working_directory_path = working_directory_path
        else:
            try:
                self.__working_directory_path = self.__data_access.load_working_directory_path()
            except:
                pass

        if self.__working_directory_path is None:
            self.__working_directory_path = pathlib.Path(__file__).resolve().parent.parent
        try:
            self.load_main()
        except:
            pass

    @property
    def get_working_directory_path(self) -> str:
        """
        Getter for the working directory path.

        Returns:
            str: the path to the current working directory.
        """
        return str(self.__working_directory_path)

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
        if not os.path.isdir(workdir):
            raise AttributeError
        self.__working_directory_path = workdir
        self.__runnables = []
        for dirpath, dirnames, filenames in os.walk(self.__working_directory_path):
            for filename in filenames:
                try:
                    if filename.endswith(".py"):
                        prog, desc, args = extract_arguments(os.path.join(dirpath, filename))
                        current_file = FileInfo(os.path.join(dirpath, filename), prog, desc, [], False)
                        for arg_name, arg_name_2, default, help_text, arg_type, required, action, choices in args:
                            current_file.add_argument(
                                Argument(arg_name, arg_name_2, default, help_text, arg_type, required, action, choices))
                        self.__runnables.append(current_file)
                except:
                    continue

        self.__data_access.save_working_directory_path(self.__working_directory_path)

    # TODO: Add some concrete type for list
    # Educated guess: a parameter with a potential value
    def save_config(self, prog: FileInfo, args: List[str or bool]) -> None:
        """
        Saves a given program and its argument to JSON.

        Args:
            prog: The program.
            args: The arguments.
        """
        saved_info = {'prog': prog.get_prog_path, 'args': args}
        self.__data_access.save_config(prog.get_prog_path, saved_info)

    def load_config(self, prog: FileInfo) -> List[str or bool]:
        """
        Loads a given program's arguments from JSON.

        Args:
            prog: The program.
        """
        res_dict = self.__data_access.load_config(prog.get_prog_path)
        return res_dict['args']

    def save_main(self):
        """
        Dumps the list of main programs to JSON.
        """
        res = dict()
        # Bit confused why we're using json to store a list
        res['main'] = [p.get_prog_path for p in self.__runnables if p.is_main_runnable]
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
        self.add_default_path()
        try:
            result = subprocess.Popen(f"python {command}", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = result.communicate()
            return stdout.decode(), stderr.decode()
        except Exception as e:
            return None, str(e)

    def clear_history(self) -> None:
        """
        Clears the configuration history.
        """
        self.__data_access.clear_history()

    def set_runnable_main_property(self, runnable: FileInfo, currently_mian: bool = False) -> None:
        """
        Sets the main property of the given runnable and saves it.

        Args:
            runnable:           The runnable.
            currently_mian:     The main property.
        """
        for idx, current_runnable in enumerate(self.__runnables):
            if runnable.get_prog_path == current_runnable.get_prog_path:
                self.__runnables[idx].set_main_runnable(currently_mian)
                self.save_main()
                self.load_main()
                return

    def get_main_runnables(self) -> List[FileInfo]:
        """
        Collects the list of main runnables.

        Returns:
            List[FileInfo]: the list of main runnables
        """
        return [r for r in self.__runnables if r.is_main_runnable]

    def search_runnable(self, given_text: str) -> List:
        """
        Searches the given_text in the list of runnables prog path.
        Args:
            given_text:  The text to be searched.

        Returns:
            List: The list of runnables that contain the given text.
        """
        if given_text == '' or len(self.__runnables) == 0:
            return []
        return self.__searching_algorithm(given_text, self.__runnables)

    @staticmethod
    def __searching_algorithm(given_text: str, runnables: List) -> List:
        """
        Searches the given_text in the list of runnables prog path.

        Args:
            given_text:      The text to be searched.
            runnables:       The list of runnables.

        Returns:
            List: The list of runnables that contain the given text.
        """
        matching = []
        for runnable in runnables:
            if given_text in runnable.get_prog_path:
                if runnable not in matching:
                    matching.append(runnable)
        return matching
