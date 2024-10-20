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
        self.data_path = os.path.join(pathlib.Path(__file__).parent.parent.parent.resolve(), 'src', 'persistence')
        self.data_access = DataAccess(self.data_path)
