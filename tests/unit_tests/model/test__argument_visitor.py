import os
import pathlib
import unittest

from src.model.argument_visitor import extract_arguments

# Full path to the test files directory
working_dir_path = os.path.join(pathlib.Path(__file__).parent.parent.parent.resolve(), 'test_files')


class TestArgumentVisitor(unittest.TestCase):
    """
    Test if the src.model.argument_visitor.extract_arguments function can extract the program name, description and
    argument details from test files. The test files are located in the test_files directory.
    """

    def test__extract_arguments_calculator(self):
        """
        Test if the extract_arguments function can extract the program name, description and argument details from the
        calculator.py file. The calculator.py file is a simple python script, which can add, subtract, multiply and
        divide two numbers.

        The test checks if the extract_arguments function can extract the program name, description and argument details
        from the calculator.py file.
        """


if __name__ == '__main__':
    unittest.main()
