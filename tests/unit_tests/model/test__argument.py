# TODO: Create unit tests for Argument class. Name the test class as TestArgument.
#  - Consider using builtin unittest library.
#  - Inherit the new class from unittest.TestCase.
#  - Create white box tests for all the getters and setters and functions.
#  - Indicate, that the file is runnable(, aka at the end of the code:
#                                         if __name__ == '__main__':
#                                            unittest.main()
import unittest
from src.model.argument import Argument


class TestArgument(unittest.TestCase):
    def test__init(self):
        """
        Testing Argument.__init__ method.
        """
        id = 'arg1'
        second_id = 'description1'
        help = 'This is a help string'
        default = 'default_value'
        required = True
        type = 'string'
        action = 'store'
        choices = ['choice1', 'choice2']

        argument = Argument(id, second_id, help, default, required, type, action, choices)

        self.assertEqual(argument.get_id, id)
        self.assertEqual(argument.get_second_id, second_id)
        self.assertEqual(argument.get_help, help)
        self.assertEqual(argument.get_default, default)
        self.assertEqual(argument.get_required, required)
        self.assertEqual(argument.get_type, type)
        self.assertEqual(argument.get_action, action)
        self.assertEqual(argument.get_choices, choices)

    def test__get_id(self):
        """
        Testing Argument.get_id method.
        """
        id = 'arg1'
        argument = Argument(id, '', '', '', False, '', '', [])

        self.assertEqual(argument.get_id, id)

    def test__get_second_id(self):
        """
        Testing Argument.get_second_id method.
        """
        second_id = 'description1'
        argument = Argument('', second_id, '', '', False, '', '', [])

        self.assertEqual(argument.get_second_id, second_id)

    def test__get_help(self):
        """
        Testing Argument.get_help method.
        """
        help = 'This is a help string'
        argument = Argument('', '', help, '', False, '', '', [])

        self.assertEqual(argument.get_help, help)

    def test__get_default(self):
        """
        Testing Argument.get_default method.
        """
        default = 'default_value'
        argument = Argument('', '', '', default, False, '', '', [])

        self.assertEqual(argument.get_default, default)

    def test__get_required(self):
        """
        Testing Argument.get_required method.
        """
        required = True
        argument = Argument('', '', '', '', required, '', '', [])

        self.assertEqual(argument.get_required, required)

