import textwrap

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from src.model.fileinfo import FileInfo
from src.model.model import Model
from src.view.style.normal_text_label import NormalTextLabel
from src.view.style.normal_text_button import NormalTextButton


class RunnerScreen(QDialog):
    """
    Screen for run the executables.
    It contains a button for step back, and text blocks to show the command and the result.

    Attributes:
        __model :      The model part of the program
        __widget:      The widget that contains the screen.
        __scroll_area: The QScrollArea widget of the screen
        __vbox:        The QVBoxLayout widget of the screen
        __runnable:    The runnable which has to be run
        __content_widget: The widget of the content.
        __command: The command which has to be executed.
    """

    def __init__(self, model: Model, widget: QtWidgets.QStackedWidget, runnable: FileInfo, command: str):
        super(RunnerScreen, self).__init__()
        self.__model = model
        self.__widget = widget
        self.__scroll_area = QtWidgets.QScrollArea()
        self.__vbox = QtWidgets.QVBoxLayout()
        self.__runnable = runnable
        self.__content_widget = QtWidgets.QWidget(widget)
        self.__command = command
        self.__init_ui()

    def __init_ui(self):
        """
        This method initializes the UI.
        """
        self.__add_back_button()
        self.__add_label('Command:\n' + self.__split_label_to_fit_screen(self.__command))
        self.__add_label('Output:\n')

        self.__content_widget.setLayout(self.__vbox)
        self.__scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.__scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.__scroll_area.setWidgetResizable(True)
        self.__scroll_area.setWidget(self.__content_widget)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.__scroll_area)
        self.setLayout(main_layout)

    def run_program(self):
        """
        This method call the run_program method of the model to run the given command.
        """
        result = self.__model.run_program(self.__command)
        for widget_idx in range(self.__vbox.count()):
            widget = self.__vbox.itemAt(widget_idx).widget()
            if isinstance(widget, NormalTextLabel):
                if widget.text().startswith('Output'):
                    if result[0] is not None:
                        result_string = result[0] + result[1]
                    else:
                        result_string = result[1]
                    widget.setText(widget.text() + result_string)

    def __add_back_button(self):
        """
        This method adds Back button to the UI and adds the suitable action to the button.
        """
        button = NormalTextButton("Back")
        self.__vbox.addWidget(button)
        button.clicked.connect(lambda: self.__back())

    def __back(self):
        """
        This method tries to go to a new RunnableConfigScreen with the runnable. If it fails, it shows an error message.
        """
        from src.view.runnable_config_screen import RunnableConfigScreen
        try:
            runnable_config_screen = RunnableConfigScreen(self.__model, self.__runnable, self.__widget)
            self.__widget.addWidget(runnable_config_screen)
            self.__widget.setCurrentIndex(self.__widget.currentIndex() + 1)
        except Exception as e:
            self.__show_message_box(f'Failed to go to another helper screen. Reason: {e}')

    def __add_label(self, text: str) -> None:
        """
        This method adds a label to the UI.
        Args:
            text: label text
        """
        label = NormalTextLabel(text)
        self.__vbox.addWidget(label)

    @staticmethod
    def __split_label_to_fit_screen(label_text: str) -> str:
        """
        This method splits the text of a label to fit on the screen.
        Args:
            label_text: Text to display

        Returns:
            str: The modified text
        """
        label_chunks = textwrap.wrap(label_text, width=130)
        label_text = ''
        for chunk in label_chunks:
            if label_text == '':
                label_text = chunk
            else:
                label_text += '\n' + chunk
        return label_text.strip()
