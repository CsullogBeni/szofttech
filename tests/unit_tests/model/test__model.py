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

        model = Model(test_path)
        model.add_default_path()
