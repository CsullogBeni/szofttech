# TODO: Create unit tests for DataAccess class. Name the test class as TestDataAccess.
#  - Consider using builtin unittest library.
#  - Inherit the new class from unittest.TestCase.
#  - Create white box tests for all the getters and setters and functions.
#  - Indicate, that the file is runnable(, aka at the end of the code:
#                                         if __name__ == '__main__':
#                                            unittest.main()
import unittest
import os
import pathlib
import json
from src.persistence.data_access import DataAccess

class TestDataAccess(unittest.TestCase):
    def setUp(self):
        self.data_path = pathlib.Path(pathlib.Path(__file__).parent.parent.parent.resolve() / 'src' / 'persistence')
        self.data_access = DataAccess(str(self.data_path))

    def test_save_config(self):
        # Test the save_config method
        runnable = "test_runnable"
        data = {"key": "value"}
        self.data_access.save_config(runnable, data)
        expected_file_path = self.data_path / "SZOFTECH" / f"{runnable.replace('/', '_').replace('\'', '_')}.json"
        self.assertTrue(os.path.exists(expected_file_path))
        with open(expected_file_path, 'r') as json_file:
            actual_data = json.load(json_file)
        self.assertEqual(actual_data, data)

    def test_load_config(self):
        # Test the load_config method
        runnable = "test_runnable"
        data = {"key": "value"}
        self.data_access.save_config(runnable, data)
        actual_data = self.data_access.load_config(runnable)
        self.assertEqual(actual_data, data)

    def test_save_main_runnables(self):
        # Test the save_main_runnables method
        data = {"key": "value"}
        self.data_access.save_main_runnables(data)
        expected_file_path = self.data_path / "SZOFTECH" / "main_runnables.json"
        self.assertTrue(os.path.exists(expected_file_path))
        with open(expected_file_path, 'r') as json_file:
            actual_data = json.load(json_file)
        self.assertEqual(actual_data, data)

    def test_load_main_runnables(self):
        # Test the load_main_runnables method
        data = {"key": "value"}
        self.data_access.save_main_runnables(data)
        actual_data = self.data_access.load_main_runnables()
        self.assertEqual(actual_data, data)

    def test_clear_history(self):
        # Test the clear_history method
        data = {"key": "value"}
        self.data_access.save_main_runnables(data)
        self.data_access.clear_history()
        expected_file_path = self.data_path / "SZOFTECH" / "main_runnables.json"
        self.assertFalse(os.path.exists(expected_file_path))

if __name__ == '__main__':
    unittest.main()