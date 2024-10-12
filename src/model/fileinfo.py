from typing import List # for the argument list
from argument import Argument  # to have access to argument class

"""
FileInfo class containing the following private variables:
 - __prog_path:           str
 - __prog_name:           str
 - __prog_description:    str
 - __args:                List[Argument]
 - __is_main_runnable:    bool
"""
class FileInfo:
    """
    Constructor for FileInfo class, that sets all variables above.
    """
    def __init__(self, prog_path: str, prog_name: str, prog_description: str, args: List[Argument], is_main_runnable: bool):
        self.__prog_path = prog_path
        self.__prog_name = prog_name
        self.__prog_description = prog_description
        self.__args = args
        self.__is_main_runnable = is_main_runnable

    """
    Getters for all the variables in FileInfo class.
    """
    def get_prog_path(self):
        return self.__prog_path

    def get_prog_name(self):
        return self.__prog_name

    def get_prog_description(self):
        return self.__prog_description

    def get_args(self):
        return self.__args

    def is_main_runnable(self):
        return self.__is_main_runnable
    """
    End of getter section.
    """

    """
    add_argument(arg: Argument) method that adds an argument to the argument list.
    """
    def add_argument(self, arg: Argument):
        contains = false
        for _arg in __args:
            if _arg == arg:
                contains = true
        if not contains:
            self.__args.append(arg)

    """
    Setter function for __is_main_runnable variable.
    """
    def set_main_runnable(self, is_main_runnable: bool):
        self.__is_main_runnable = is_main_runnable