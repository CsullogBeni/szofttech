from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog

from src.model.fileinfo import FileInfo
from src.model.model import Model


# TODO: Create __init_ui(clear: Bool) method, that initializes the UI.
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
    def __init__(self, model: Model, runnable: FileInfo, widget: QtWidgets.QStackedWidget, clear: bool = False):
        super(RunnableConfigScreen, self).__init__()

        self.__model = model
        self.__runnable = runnable
        self.__widget = widget
        self.__scroll_area = QtWidgets.QScrollArea(self)
        self.__vbox = QtWidgets.QVBoxLayout(self)
        self.__button_widget = QtWidgets.QWidget(self)

        self.__init_ui(clear)
