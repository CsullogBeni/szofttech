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

        model = Model(test_path)
        self.assertEqual(model.get_working_directory_path, test_path)
