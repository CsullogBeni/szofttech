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
        self.assertEqual(len(model.get_runnables), 2)
        self.assertEqual(model.get_runnables[0].get_prog_path, test_path + '\\calculator\\calculator.py')
        self.assertEqual(model.get_runnables[0].is_main_runnable, False)
        self.assertEqual(len(model.get_runnables[0].get_args), 3)
        self.assertEqual(model.get_runnables[0].get_args[2].get_id, '--operation')
        self.assertIn('This program can add', model.get_runnables[0].get_prog_description)
        self.assertEqual(model.get_runnables[0].get_prog_name, 'Calculator')
        self.assertEqual(model.get_runnables[1].get_prog_path, test_path + '\\minmax\\minmax.py')
        self.assertEqual(model.get_runnables[1].is_main_runnable, False)
        self.assertEqual(len(model.get_runnables[1].get_args), 2)
        self.assertEqual(model.get_runnables[1].get_args[1].get_id, 'numbers')
        self.assertIn('This program can select', model.get_runnables[1].get_prog_description)
        self.assertEqual(model.get_runnables[1].get_prog_name, 'Minmax')

    def test__save_config(self):

        model = Model()
        arg1 = Argument('arg1', 'description1', '', '', False, '', '', [])
        arg2 = Argument('arg2', 'description2', '', '', False, '', '', [])
        prog = FileInfo('/path/to/program', 'Program Name', 'This is a program', [arg1, arg2], False)
        args = [('arg1', 'value1'), ('arg2', 'value2')]

        model.save_config(prog, args)

        res_dict = model.get_data_access.load_config(prog.get_prog_path)
        self.assertEqual(res_dict, {'arg1': 'value1', 'arg2': 'value2'})


if __name__ == '__main__':
    unittest.main()
