from typing import List  # for the argument list
from src.model.argument import Argument  # to have access to argument class


class FileInfo:
    """
    Contains all the data about a runnable.
    
    Attributes:
        __prog_path:           the path to the runnable
        __prog_name:           the name of the runnable
        __prog_description:    the description of a runnable
        __args:                the argument list of the runnable
        __is_main_runnable:    indicates if it is a main runnable
    """

    def __init__(self, prog_path: str, prog_name: str, prog_description: str, args: List[Argument],
                 is_main_runnable: bool):
        self.__prog_path = prog_path
        self.__prog_name = prog_name
        self.__prog_description = prog_description
        self.__args = args
        self.__is_main_runnable = is_main_runnable

    @property
    def get_prog_path(self):
        """
        Getter for the file path of the runnable.

        Returns:
            str: the path of the runnable
        """
        return self.__prog_path

    @property
    def get_prog_name(self):
        """
        Getter for the name of the runnable.

        Returns:
            str: the name of the runnable
        """
        return self.__prog_name

    @property
    def get_prog_description(self):
        """
        Getter for the description of the runnable.

        Returns:
            str: the description of the runnable
        """
        return self.__prog_description

    @property
    def get_args(self):
        """
        Getter for the argument list of the runnable.

        Returns:
            List[Argument]: the argument list of the runnable
        """
        return self.__args

    @property
    def is_main_runnable(self):
        """
        Getter for the main runnable flag of the runnable.

        Returns:
            bool: the main runnable flag of the runnable
        """
        return self.__is_main_runnable

    def add_argument(self, arg: Argument):
        """
        Adds an argument to the argument list if it's not already added.

        Args:
            arg (Argument): the argument to be added to the argument list
        """
        contains = False
        for _arg in self.__args:
            if _arg == arg:
                contains = True
        if not contains:
            self.__args.append(arg)

    def set_main_runnable(self, is_main_runnable: bool):
        """
        Setter for the main runnable flag

        Args:
            is_main_runnable (bool): the value to which the flag must be set
        """
        self.__is_main_runnable = is_main_runnable
