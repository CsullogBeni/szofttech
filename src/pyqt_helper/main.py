import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets

from src.pyqt_helper.helper_screen import HelperScreen


def main():
    """
    I am a main function that is used to initialize the program.
    Initialize a QApplication object, name it as app.
    Initialize a QtWidgets.QStackedWidget, name it as widget, that will be used for changing windows.
    Initialize the HelperScreen that contains the UI of the program.
    """
    app = QApplication(sys.argv)
    app.setApplicationName('I am a PyQt helper app')
    widget = QtWidgets.QStackedWidget()
    helper_screen = HelperScreen(widget)
    widget.setFixedWidth(1200)
    widget.setFixedHeight(800)
    widget.addWidget(helper_screen)
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


