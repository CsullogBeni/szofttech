from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog


class AnotherHelperScreen(QDialog):
    """
    Screen that contains a scroll area.
    """
    def __init__(self, widget: QtWidgets.QStackedWidget):
        super(AnotherHelperScreen, self).__init__()
        self.__widget = widget
        self.__outer_vbox = QtWidgets.QVBoxLayout()
        self.__scroll_area = QtWidgets.QScrollArea()
        self.__init_ui()

    def __init_ui(self):
        """
        Initializes the scroll area UI.
        """
        self.__scroll_area.setMaximumWidth(1200)
        self.__outer_vbox.addWidget(self.__scroll_area)
        self.__add_buttons_to_scroll_area()
        self.setLayout(self.__outer_vbox)

    def __add_buttons_to_scroll_area(self):
        """
        This is not the best example how to handle a scroll area. But it works.
        You can create a new method for this.
        """
        button_widget = QtWidgets.QWidget()
        inner_vbox = QtWidgets.QVBoxLayout()
        for i in range(50):
            button = QtWidgets.QPushButton(f'Button {i+1}')
            inner_vbox.addWidget(button)
        self.__scroll_area.setWidgetResizable(True)
        button_widget.setLayout(inner_vbox)
        self.__scroll_area.setWidget(button_widget)
