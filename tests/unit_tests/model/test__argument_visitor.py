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
        self.assertEqual(args[0], ('--number1', '-n1', None, 'First number to do operation with', 'float', True, None,
                                   []))
        self.assertEqual(args[1], ('--number2', '-n2', None, 'Second number to do operation with', 'float', False, None,
                                   []))
        self.assertEqual(args[2], ('--operation', '-o', '+', 'Operation, which can be: +, -, *, /', None, False, None,
                                   ['+', '-', '*', '/']))

    def test__extract_arguments_minmax(self):
        """
        Test if the extract_arguments function can extract the program name, description and argument details from the
        minmax.py file. The minmax.py file is a simple python script, which can select the maximum or the minimum from
        the given numbers.

        The test checks if the extract_arguments function can extract the program name, description and argument details
        from the minmax.py file.
        """
        minmax_path = os.path.join(working_dir_path, 'minmax', 'minmax.py')
        prog, desc, args = extract_arguments(minmax_path)
        self.assertEqual(prog, 'Minmax')
        self.assertEqual(desc,
                         'This program can select the maximum or the minimum from the given numbers. Numbers' +
                         ' given from the user as the command line arguments. The program select maximum by ' +
                         'default, but user can ask minimum by --min flag. The result is printed to the console.')
        self.assertEqual(len(args), 2)
        self.assertEqual(args[0], ('--min', '-m', None, 'Whether user wants minimum selection', None, False,
                                   'store_true', []))
        self.assertEqual(args[1], ('--numbers', None, None, 'Numbers to select maximum or minimum from', 'float',
                                   False, None, []))

    def test__extract_arguments_randomlist(self):
        """
        Test if the extract_arguments function can extract the program name, description and argument details from the
        randomlist.py file. The randomlist.py file is a simple python script, which generates a list of random integers.

        The test checks if the extract_arguments function can extract the program name, description and argument details
        from the randomlist.py file.
        """
        randomlist_path = os.path.join(working_dir_path, 'randomlist', 'randomlist.py')
        prog, desc, args = extract_arguments(randomlist_path)
        self.assertEqual(prog, 'Random List Generator')
        self.assertEqual(desc, 'Generates a random list of integers')
        self.assertEqual(len(args), 3)
        self.assertEqual(args[0], ('--count', '-c', None, 'How many integers to generate', 'int', True, None,
                                   []))
        self.assertEqual(args[1], ('--lowerbound', '-lb', 0, 'Lower bound, defaults to 0', 'int', False, None,
                                   []))
        self.assertEqual(args[2], ('--upperbound', '-ub', 2147483647, 'Upper bound, defaults to the integer limit', 'int', False, None,
                                   []))


if __name__ == '__main__':
    unittest.main()
