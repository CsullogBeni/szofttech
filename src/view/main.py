# TODO: Create the main function of the program.
#  - Import QApplication and QtWidgets from PyQt5 library, name it as app.
#  - main function should initialize a QApplication object, name it as widget.
#  - main function should initialize a QtWidgets.QStackedWidget, it will used for changing windows.
#  - main function should initialize a Model object, that will be used in the whole runtime.
#  - main function should call widget.show().
#  - Don't forget to write to the end of main the following: sys.exit(app.exec_()9
#  - Indicate, that the file is runnable(, aka at the end of the code:
#                                         if __name__ == '__main__':
#                                            main()

import sys
import pathlib
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from src.model.model import Model
from src.view.show_runnables_screen import ShowRunnablesScreen


def main():
    """
    Main function of the program. Initialize the User interface.
    """
    app = QApplication(sys.argv)
    app.setApplicationName('PyRun')
    widget = QtWidgets.QStackedWidget()
    model = Model()
    project_path = pathlib.Path(__file__).parent.parent.parent.absolute()
    showrunnablescreen = ShowRunnablesScreen(model, widget, str(project_path) + '/tests/test_files')
    widget.addWidget(showrunnablescreen)
    widget.setFixedWidth(1200)
    widget.setFixedHeight(800)
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
