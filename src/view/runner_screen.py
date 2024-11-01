from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from src.model.fileinfo import FileInfo
from src.model.model import Model
from src.view.style.normal_text_label import NormalTextLabel


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
        __button_widget: The widget that contains the button.
        __command: The command which has to be executed.
    """

    def __init__(self, model: Model, widget: QtWidgets.QStackedWidget, runnable: FileInfo, command: str):
        super(RunnerScreen, self).__init__()
        self.__model = model
        self.__widget = widget
        self.__scroll_area = QtWidgets.QScrollArea()
        self.__vbox = QtWidgets.QVBoxLayout()
        self.__runnable = runnable
        self.__button_widget = QtWidgets.QWidget(widget)
        self.__command = command
        self.__init_ui()

    def __init_ui(self):
        """
        This method initializes the UI.
        """
        self.__add_back_button()
        self.__add_label('Command:\n' + self.__command)
        self.__add_label('Output:\n')
        self.setLayout(self.__vbox)

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
        button = QtWidgets.QPushButton("Back")
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
