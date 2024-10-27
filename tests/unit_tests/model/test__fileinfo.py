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

    def test__get_prog_name(self):
        """
        Testing FileInfo.get_prog_name method.
        """
        prog_name = 'Program Name'
        file_info = FileInfo('/path/to/program', prog_name, 'This is a program', [], False)

        self.assertEqual(file_info.get_prog_name, prog_name)

    def test__get_prog_description(self):
        """
        Testing FileInfo.get_prog_description method.
        """
        prog_description = 'This is a program'
        file_info = FileInfo('/path/to/program', 'Program Name', prog_description, [], False)

        self.assertEqual(file_info.get_prog_description, prog_description)

    def test__get_args(self):
        """
        Testing FileInfo.get_args method.
        """
        arg1 = Argument('arg1', 'description1', '', '', False, '', '', [])
        arg2 = Argument('arg1', 'description1', '', '', False, '', '', [])
        args = [arg1, arg2]
        file_info = FileInfo('/path/to/program', 'Program Name', 'This is a program', args, False)

        self.assertEqual(file_info.get_args, args)

    def test__is_main_runnable(self):
        """
        Testing FileInfo.is_main_runnable method.
        """
        is_main_runnable = True
        file_info = FileInfo('/path/to/program', 'Program Name', 'This is a program', [], is_main_runnable)

        self.assertEqual(file_info.is_main_runnable, is_main_runnable)

    def test__set_main_runnable(self):
        """
        Testing FileInfo.set_main_runnable method.
        """
        is_main_runnable = True
        file_info = FileInfo('/path/to/program', 'Program Name', 'This is a program', [], False)

        file_info.set_main_runnable(is_main_runnable)
        self.assertEqual(file_info.is_main_runnable, is_main_runnable)

