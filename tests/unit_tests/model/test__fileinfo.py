# TODO: Create unit tests for FileInfo class. Name the test class as TestFileInfo.
#  - Consider using builtin unittest library.
#  - Inherit the new class from unittest.TestCase.
#  - Create white box tests for all the getters and setters and functions.
#  - Indicate, that the file is runnable(, aka at the end of the code:
#                                         if __name__ == '__main__':
#                                            unittest.main()
import unittest
from src.model.fileinfo import FileInfo
from src.model.argument import Argument

class TestFileInfo(unittest.TestCase):
    """
    Test class for the src.model.FileInfo object.
    """

    def test__init(self):
        """
        Testing FileInfo.__init__ method.
        """
        prog_path = '/path/to/program'
        prog_name = 'Program Name'
        prog_description = 'This is a program'
        args = [Argument('arg1', 'description1', '', '', False, '', '', [])]
        is_main_runnable = True

        file_info = FileInfo(prog_path, prog_name, prog_description, args, is_main_runnable)

        self.assertEqual(file_info.get_prog_path, prog_path)
        self.assertEqual(file_info.get_prog_name, prog_name)
        self.assertEqual(file_info.get_prog_description, prog_description)
        self.assertEqual(file_info.get_args, args)
        self.assertEqual(file_info.is_main_runnable, is_main_runnable)

    def test__get_prog_path(self):
        """
        Testing FileInfo.get_prog_path method.
        """
        prog_path = '/path/to/program'
        file_info = FileInfo(prog_path, 'Program Name', 'This is a program', [], False)

        self.assertEqual(file_info.get_prog_path, prog_path)

