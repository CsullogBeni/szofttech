import unittest
import os
import json
from src.persistence.data_access import DataAccess


class TestDataAccess(unittest.TestCase):
    def setUp(self) -> None:
        self.data_path = os.path.join(os.environ['LOCALAPPDATA'], "SZOFTECH")
        self.data_access = DataAccess()

    def test_save_config(self) -> None:
        """
        Test the save_config method by storing data for a specific runnable.

        Checks if the data is successfully saved to a JSON file and loaded correctly.

        Args:
            self: The test case instance.
        """
        runnable = "test_runnable"
        data = {"key": "value"}
        self.data_access.save_config(runnable, data)
        expected_file_path = os.path.join(self.data_path, (runnable.replace('/', '').replace(",", '_') + ".json"))
        self.assertTrue(os.path.exists(expected_file_path))
        with open(expected_file_path, 'r') as json_file:
            actual_data = json.load(json_file)
        self.assertEqual(actual_data, data)

    def test_load_config(self) -> None:
        """
        Test the load_config method by loading data for a specific runnable.

        Checks if the data is successfully loaded from a JSON file.

        Args:
            self: The test case instance.
        """
        runnable = "test_runnable"
        data = {"key": "value"}
        self.data_access.save_config(runnable, data)
        actual_data = self.data_access.load_config(runnable)
        self.assertEqual(actual_data, data)

    def test_save_main_runnables(self) -> None:
        """
        Test the save_main_runnables method by storing data to a JSON file.

        Checks if the data is successfully saved to the correct location.

        Args:
            self: The test case instance.
        """
        data = {"key": "value"}
        self.data_access.save_main_runnables(data)
        expected_file_path = os.path.join(self.data_path, "main_runnables.json")
        self.assertTrue(os.path.exists(expected_file_path))
        with open(expected_file_path, 'r') as json_file:
            actual_data = json.load(json_file)
        self.assertEqual(actual_data, data)

    def test_load_main_runnables(self) -> None:
        """
        Test the load_main_runnables method by loading data from a JSON file.

        Checks if the data is successfully loaded from the correct location.

        Args:
            self: The test case instance.
        """
        data = {"key": "value"}
        self.data_access.save_main_runnables(data)
        actual_data = self.data_access.load_main_runnables()
        self.assertEqual(actual_data, data)

    def test_clear_history(self) -> None:
        """
        Test the clear_history method by clearing the history and checking that the
        configuration file is deleted.

        Args:
            self: The test case instance.
        """
        data = {"key": "value"}
        self.data_access.save_main_runnables(data)
        self.data_access.clear_history()
        expected_file_path = os.path.join(self.data_path, "main_runnables.json")
        self.assertFalse(os.path.exists(expected_file_path))


if __name__ == '__main__':
    unittest.main()
