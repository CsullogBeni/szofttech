from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog

from src.pyqt_helper.another_helper_screen import AnotherHelperScreen

"""
Important: Be careful with circular import. If an error message indicates that there is a circular import, then
you can make imports within a function or method to avoid this problem. 
"""


class HelperScreen(QDialog):
    """
    Example screen, that contains many UI elements.
    """
    def __init__(self, widget: QtWidgets.QStackedWidget):
        super(HelperScreen, self).__init__()
        self.__widget = widget                           # This helps to change screens
        self.__outer_vbox = QtWidgets.QVBoxLayout()
        self.__init_ui()

    def __init_ui(self):
        """
        This method initializes the UI.
        """
        self.__add_label('I am a label')
        self.__add_modified_label()
        self.__add_button('I am a button')
        self.__add_horizontal_layout()
        self.__add_grid_layout()
        self.__add_screen_change_button()
        self.__add_combo_box()
        self.setLayout(self.__outer_vbox)

    def __add_label(self, text: str):
        """
        This method adds a label to the UI.
        Args:
            text: label text
        """
        label = QtWidgets.QLabel(text)
        self.__outer_vbox.addWidget(label)

    def __add_modified_label(self):
        """
        This method adds a fany bold dark blue 24px label to the UI.
        """
        label = QtWidgets.QLabel(
            "<b><span style='color: darkblue; font-size: 24px;'>I am bold 24px dark blue text</span></b>")
        self.__outer_vbox.addWidget(label)

    def __add_button(self, text: str):
        """
        This method adds a button to the UI and adds an action to the button.
        Args:
            text: button text
        """
        button = QtWidgets.QPushButton(text)
        self.__outer_vbox.addWidget(button)
        # This might cause a reference warning, but in runtime the interpreter can recognize the method.
        button.clicked.connect(lambda: self.__show_message_box('I am a message box, also a button action'))

    @staticmethod
    def __show_message_box(text: str):
        """
        Shows a message box. Useful fact: OK or CANCEL button can be added to the message box as well.
        Args:
            text: message box text
        """
        msg_box = QtWidgets.QMessageBox()
        msg_box.setText(text)
        msg_box.exec()

    def __add_horizontal_layout(self):
        """
        This method adds a horizontal layout to the UI.
        """
        hbox = QtWidgets.QHBoxLayout()
        for idx in range(5):
            button = QtWidgets.QPushButton(f'Button {idx} in horizontal layout')
            hbox.addWidget(button)
        self.__outer_vbox.addLayout(hbox)

    def __add_grid_layout(self):
        """
        This method adds a grid layout to the UI. In grid layout you can position widgets in rows and columns.
        """
        grid = QtWidgets.QGridLayout()
        for idx in range(6):
            button = QtWidgets.QPushButton(f'Button {idx} in grid layout')
            grid.addWidget(button, idx // 3, idx % 3)
        self.__outer_vbox.addLayout(grid)

    def __add_screen_change_button(self):
        """
        This method adds a button to change the screen and adds the __go_to_another_helper_screen action to the button.
        """
        button = QtWidgets.QPushButton('Go to another helper screen')
        button.clicked.connect(self.__go_to_another_helper_screen)
        self.__outer_vbox.addWidget(button)

    def __go_to_another_helper_screen(self):
        """
        This method tries to go to another helper screen. If it fails, it shows an error message.
        """
        try:
            another_helper_screen = AnotherHelperScreen(self.__widget)
            self.__widget.addWidget(another_helper_screen)
            self.__widget.setCurrentIndex(self.__widget.currentIndex() + 1)
        except Exception as e:
            self.__show_message_box(f'Failed to go to another helper screen. Reason: {e}')

    def __add_combo_box(self):
        """
        This method adds a combo box to the UI.
        """
        combo_box = QtWidgets.QComboBox()
        combo_box.addItem('Item 1')
        combo_box.addItem('Item 2')
        combo_box.addItem('Item 3')
        self.__outer_vbox.addWidget(combo_box)
