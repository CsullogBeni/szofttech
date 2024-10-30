from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from src.model.fileinfo import FileInfo
from src.model.model import Model
from src.view.style.normal_text_button import NormalTextButton
from src.view.style.normal_text_label import NormalTextLabel
from src.view.style.title_text_label import TitleTextLabel


# TODO: Implement the __go_to_show_runnables_screen() method. This should initialize a new ShowRunnablesScreen.
# TODO: Implement the __show_prog_args(clear: Bool) method, that shows the arguments of the given runnable.
# TODO: Implement the __split_argument_label_info(arg_description: String) method. This should split description to fit
#   on the screen

# TODO: Implement the __add_arg_desc_style() method that ads style to the string (similar like html)
# TODO: Implement the __add_input_field(arg: Argument) method. This should add a input field to the screen.
# TODO: Implement the __equip_button_action(button: QtButton) method. This should add aa button to the screen.
# TODO: Implement the __add_vertical_spacing(space_gap: Int) method. The vertical spacing should be added to the screen
#  between arguments.
# TODO: Implement the __run_configuration() method. This should initialize a new RunnerScreen.

# TODO: Implement the extract_argument(text: String) static method, that filters the the argument name from the
#  argument's detail.
# TODO: Implement the remove_text_in_angle_brackets(text: String) static method, that removes the angle brackets.
#  Usually xml/html codes are located between angle brackets.
# TODO: Implement the __clear_args() method that clears all the input fields and initialize a new RunnableConfigScreen
#  with the same runnable.
# TODO: Implement the __save_config() method. This should save the given runnable's configuration.
# TODO: Implement the __load_config() method. This should load the given runnable's configuration.
# TODO: Implement the list_reducer(arg_list: List) static method, deletes the first item of the list.

class RunnableConfigScreen(QDialog):
    """
    This screen will show the configuration of a runnable. All the arguments, and its details.

    Attributes:
        __model:       The model of the program.
        __widget:      The widget that contains the screen
        __scroll_area: The QScrollArea widget of the screen
        __vbox:        The QScrollArea widget of the screen
        __runnable:    The runnable whose configuration has to be shown
        __button_widget: The widget that contains button
    """

    def __init__(self, model: Model, runnable: FileInfo, widget: QtWidgets.QStackedWidget, clear: bool = False):
        super(RunnableConfigScreen, self).__init__()

        self.__model = model
        self.__runnable = runnable
        self.__widget = widget
        self.__scroll_area = QtWidgets.QScrollArea(self)
        self.__vbox = QtWidgets.QVBoxLayout(self)
        self.__button_widget = QtWidgets.QWidget(self)

        self.__init_ui(clear)

    def __init_ui(self, clear: bool) -> None:
        """
        This method initializes the UI.
        Args:
            clear: This parameter decides whether the configuration of the given runnable has to be loaded.
                    It will be passed to __show_prog_details method.
        Returns:
            None
        """
        self.__scroll_area.setMaximumWidth(1200)
        self.__show_prog_details(clear)
        button = NormalTextButton('Clear history')
        button.clicked.connect(self.__clear_args())
        self.__vbox.addWidget(button)
        button = NormalTextButton('Run')
        button.clicked.connect(self.__run_configuration())
        self.__vbox.addWidget(button)
        button = NormalTextButton('Back')
        button.clicked.connect(self.__go_to_show_runnables_screen())
        self.__vbox.addWidget(button)

        self.__button_widget.setLayout(self.__vbox)
        self.__scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.__scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.__scroll_area.setWidgetResizable(True)
        self.__scroll_area.setWidget(self.__button_widget)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.__scroll_area)
        self.setLayout(main_layout)

    @staticmethod
    def __get_dark_blue_label_text(text: str) -> str:
        """
        This method wrap the text into a dark blue span.
        Args:
            text: The text which has to be displayed dark blue

        Returns:
            str: The wrapped text
        """
        return "<b><span style='color: darkblue'>" + text + "</span></b>"

    def __show_prog_details(self, clear: bool) -> None:
        """
        This method add the details of the runnable which has to be executed to the UI.
        Args:
            clear: This parameter decides whether the configuration of the given runnable has to be loaded.
                    It will be passed to __show_prog_args method.

        Returns:
            None
        """
        runnable_path = TitleTextLabel(self.__get_dark_blue_label_text("Fullpath: ") + self.__runnable.get_prog_path)
        runnable_path.setMaximumWidth(1100)
        runnable_prog = NormalTextLabel(self.__get_dark_blue_label_text("Program: ") + self.__runnable.get_prog_name)
        runnable_prog.setMaximumWidth(1100)
        description = self.split_argument_label_info(self.__runnable.get_prog_description)
        runnable_desc = NormalTextLabel(self.__get_dark_blue_label_text("Program's description: ") + description)
        runnable_desc.setMaximumWidth(1100)
        self.__vbox.addWidget(runnable_path)
        self.__vbox.addWidget(runnable_prog)
        self.__vbox.addWidget(runnable_desc)
        self.__add_vertical_spacing()
        self.__show_prog_args(clear)
