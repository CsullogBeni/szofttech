# TODO: Create unit tests for DataAccess class. Name the test class as TestDataAccess.
#  - Consider using builtin unittest library.
#  - Inherit the new class from unittest.TestCase.
#  - Create white box tests for all the getters and setters and functions.
#  - Indicate, that the file is runnable(, aka at the end of the code:
#                                         if __name__ == '__main__':
#                                            unittest.main()
import os
import pathlib
import unittest

# Full path to the test files directory
working_dir_path = os.path.join(pathlib.Path(__file__).parent.parent.parent.resolve(), 'test_files')

class TestDataAccess(unittest.TestCase):