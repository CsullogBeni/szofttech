import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from src.model.model import Model
from src.view.show_runnables_screen import ShowRunnablesScreen

def main():
    """
    Main function of the program. Initialize the User interface.
    """
    app = QApplication(sys.argv)
    app.setApplicationName('PyRunner')
    widget = QtWidgets.QStackedWidget()
    model = Model()
    show_runnable_screen = ShowRunnablesScreen(model, widget)
    widget.addWidget(show_runnable_screen)
    widget.setFixedWidth(1200)
    widget.setFixedHeight(800)
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
