import os
import pathlib
import sys
import unittest

from src.model.model import Model
from src.model.fileinfo import FileInfo
from src.model.argument import Argument

test_path = os.path.join(pathlib.Path(__file__).resolve().parent.parent.parent, 'test_files')


class TestModel(unittest.TestCase):

    def test__init(self):
        """
        Testing Model.__init__ method.
        """
        model = Model()

        self.assertIsNotNone(model.get_data_access)
        self.assertEqual(model.get_runnables, [])

    def test__get_working_directory_path(self):
        """
        Testing Model.get_working_directory_path method.
        """
        model = Model(test_path)
        self.assertEqual(model.get_working_directory_path, test_path)

    def test__get_runnables(self):
        """
        Testing Model.get_runnables method.
        """
        model = Model()
        prog = FileInfo('/path/to/program', 'Program Name', 'This is a program', [], False)
        model.get_runnables.append(prog)

        self.assertEqual(model.get_runnables, [prog])

    def test__get_data_access(self):
        """
        Testing Model.get_data_access method.
        """
        model = Model()
        self.assertIsNotNone(model.get_data_access)

    def test__add_default_path(self):
        """
        Testing Model.add_default_path method.
        """
        model = Model(test_path)
        model.add_default_path()

    def test__add_working_directory_path(self):
        """
        Testing Model.add_working_directory_path method.
        """
        model = Model(test_path)
        model.add_working_directory_path(test_path)
        self.assertEqual(model.get_working_directory_path, test_path)
        self.assertEqual(len(model.get_runnables), 7)
        self.assertEqual(model.get_runnables[1].get_prog_path, test_path + '\\calculator\\calculator.py')
        self.assertEqual(len(model.get_runnables[1].get_args), 3)
        self.assertIn('This program can add', model.get_runnables[1].get_prog_description)
        self.assertEqual(model.get_runnables[1].get_prog_name, 'Calculator')
        self.assertEqual(model.get_runnables[4].get_prog_path, test_path + '\\minmax\\minmax.py')
        self.assertEqual(len(model.get_runnables[4].get_args), 2)
        self.assertEqual(model.get_runnables[4].get_args[1].get_id, '--numbers')
        self.assertIn('This program can select', model.get_runnables[4].get_prog_description)
        self.assertEqual(model.get_runnables[4].get_prog_name, 'Minmax')

    def test__save_config(self):
        """
        Testing Model.save_config method.
        """
        model = Model()
        arg1 = Argument('arg1', 'description1', '', '', False, '', '', [])
        arg2 = Argument('arg2', 'description2', '', '', False, '', '', [])
        prog = FileInfo('/path/to/program', 'Program Name', 'This is a program', [arg1, arg2], False)
        args = [('arg1', 'value1'), ('arg2', 'value2')]

        model.save_config(prog, args)

        res_dict = model.get_data_access.load_config(prog.get_prog_path)
        self.assertEqual(res_dict, {'args': [['arg1', 'value1'], ['arg2', 'value2']], 'prog': '/path/to/program'})

    def test__load_config(self):
        """
        Testing Model.load_config method.
        """
        model = Model()
        arg1 = Argument('arg1', 'description1', '', '', False, '', '', [])
        arg2 = Argument('arg2', 'description2', '', '', False, '', '', [])
        prog = FileInfo('/path/to/program', 'Program Name', 'This is a program', [arg1, arg2], False)
        args = [('arg1', 'value1'), ('arg2', 'value2')]

        model.save_config(prog, args)

        loaded_args = model.load_config(prog)

        self.assertEqual(loaded_args, {'args': [['arg1', 'value1'], ['arg2', 'value2']], 'prog': '/path/to/program'})

    def test__load_main(self):
        """
        Testing Model.load_main method.
        """
        model = Model()
        prog = FileInfo('/path/to/program', 'Program Name', 'This is a program', [], True)
        model.get_runnables.append(prog)

        model.save_main()
        prog.set_main_runnable(False)
        model.load_main()
        prog = model.get_runnables[0]

        self.assertTrue(prog.is_main_runnable)

    def test__run_program(self):
        """
        Testing Model.run_program method.
        """
        model = Model(test_path)
        model.add_working_directory_path(test_path)
        calculator_path = os.path.join(test_path, 'calculator', 'calculator.py')
        command = calculator_path + ' --number1 1 --number2 2 --operation +'
        std_out, std_err = model.run_program(command)
        self.assertEqual(std_out, 'Result: 1.0 + 2.0 = 3.0\r\n')
        self.assertEqual(std_err, '')
        std_out, std_err = model.run_program(calculator_path)
        self.assertEqual(std_out, '')
        self.assertIn('-h] --number1 NUMBER1 [--number2 NUMBER2]', std_err)

    def test__search_runnables(self):
        """
        Testing Model.search_runnables method.
        """
        model = Model(test_path)
        model.add_working_directory_path(test_path)
        self.assertEqual(model.search_runnable('calculator'), [model.get_runnables[1]])


if __name__ == '__main__':
    unittest.main()
