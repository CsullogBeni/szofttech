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
        calculator_path = os.path.join(working_dir_path, 'calculator', 'calculator.py')
        prog, desc, args = extract_arguments(calculator_path)
        self.assertEqual(prog, 'Calculator')
        self.assertEqual(desc,
                         'This program can add, subtract, multiply and divide two numbers. Numbers and' +
                         ' operators given from the user as the command line arguments. The result is ' +
                         'printed to the console.')
        self.assertEqual(len(args), 3)
        self.assertEqual(args[0], ('--number1', None, None, 'First number to do operation with', 'float', True, None,
                                   []))
        self.assertEqual(args[1], ('number2', None, None, 'Second number to do operation with', 'float', False, None,
                                   []))
        self.assertEqual(args[2], ('--operation', None, '+', 'Operation, which can be: +, -, *, /', None, False, None,
                                   ['+', '-', '*', '/']))




if __name__ == '__main__':
    unittest.main()
