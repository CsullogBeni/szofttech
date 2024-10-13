from typing import List


class Argument:
    """
    Represents a command-line argument of a runnable.

    Attributes:
        __id:              the identifier of the argument
        __second_id:       the second identifier of the argument
        __help:            a short description of what the argument does
        __default:         the value produced if the argument was not specified from the command lin
        __required:        whether the argument is mandatory
        __type:            the type to which the argument should be converted
        __action:          the basic type of action to be taken when this argument is encountered at the command line
        __choices:         a list of the allowable values for the argument
    """

    def __init__(self, id: str, second_id: str, help: str, default: str, required: bool,
                 type: str, action: str, choices: List[str]):
        self.__id = id
        self.__second_id = second_id
        self.__help = help
        self.__default = default
        self.__required = required
        self.__type = type
        self.__action = action
        self.__choices = choices

    @property
    def get_id(self):
        """
        Getter for the id of the argument.

        Returns:
            str: the id of the argument
        """
        return self.__id

    @property
    def get_second_id(self):
        """
        Getter for the second_id of the argument.

        Returns:
            str: the second_id of the argument
        """
        return self.__second_id

    @property
    def get_help(self):
        """
        Getter for the help string of the argument.

        Returns:
            str: the help string of the argument
        """
        return self.__help

    @property
    def get_default(self):
        """
        Getter for the default value of the argument.

        Returns:
            str: the default value of the argument
        """
        return self.__default

    @property
    def get_required(self):
        """
        Getter whether the argument is required.

        Returns:
            bool: whether the argument is required
        """
        return self.__required

    @property
    def get_type(self):
        """
        Getter for the type of the argument.

        Returns:
            str: the type of the argument
        """
        return self.__type

    @property
    def get_action(self):
        """
        Getter for the action of the argument.

        Returns:
            str: the action of the argument
        """
        return self.__action

    @property
    def get_choices(self):
        """
        Getter for the list of the choices of the argument.

        Returns:
            List[str]: the list of the choices of the argument
        """
        return self.__choices
