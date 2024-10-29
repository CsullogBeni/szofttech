# TODO: Create ShowRunnablesScreen class. The screen should show all the runnables and, main runnables prioritized.
#  Search bar should be added. Clear history button should be added as well.
#  It should contain the following private variables:
#  - __model:       Model
#  - __widget:      QtWidgets.QStackedWidget
#  - __scroll_area: QtWidgets.QScrollArea
#  - __vbox:        QtWidgets.QVBoxLayout

# TODO: Inherit the current class from QtWidgets.QDialog.
# TODO: Create constructor for ShowRunnablesScreen class, that sets all variables above.
# TODO: Create __init_ui(searched_runnables: List) method, that initializes the UI.
# TODO: Implement the add_found_runnables(searched_runnables: List) method. After searching, the found ones should be
#  added to the screen first, then the main runnables.
# TODO: Implement the add_search_bar() method. The search bar and a search button should be added to the screen.
# TODO: Add the __search() function, that calls the model's search_runnables() method.
# TODO: Implement the __vertical_spacing(space_gap: Int) method. The vertical spacing should be added to the screen
#  between the search bar, the main runnables and the normal runnables.
# TODO: Implement the __try_load_runnable(runnable: FileInfo) method. This should initialize a RunnableConfigScreen with
#  the given runnable.
# TODO: Implement the __set_main(runnable: FileInfo) method. This should set the given runnable as main.
# TODO: Implement the __unset_main(runnable: FileInfo) method. This should unset the given runnable as main.
# TODO: Implement the __clear_history() method. This should clear the history.
# TODO: Implement the __show_runnables_screen(searched_runnables: List) method. This should list all the runnables for
#  the user, searched runnables and main runnables should be prioritized.
# TODO: Implement the __show_message(message: str) static method. This should show the given message to the user.


from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from typing import List
from PyQt5.QtWidgets import QDialog

from src.model.fileinfo import FileInfo
from src.model.model import Model
# from src.view.runnable_config_screen import RunnableConfigScreen
# from src.view.style.normal_text_label import NormalTextLabel
from src.view.style.normal_text_button import NormalTextButton


class ShowRunnablesScreen(QDialog):
    def __init__(self, model: Model, widget: QtWidgets.QStackedWidget, working_dir_path: str = '',
                 searched_runnables: List = None) -> None:
        super(ShowRunnablesScreen, self).__init__()
        if working_dir_path:
            self.__model = Model(working_dir_path)
        else:
            self.__model = model
        self.__model.add_working_directory_path(self.__model.get_working_directory_path)
        self.__widget = widget
        self.__scroll_area = None
        self.__vbox = None
        self.__button_widget = None
        self.___init_ui()

    def ___init_ui(self) -> None:
        self.__scroll_area = QtWidgets.QScrollArea()
        self.__button_widget = QtWidgets.QWidget()
        self.__vbox = QtWidgets.QVBoxLayout()

        self.__add_working_dir_input()
        self.__add_vertical_spacing(20)

        """
        search bar field
        """

        """
        favourite runnables field
        """

        '''main_counter = 0
        for runnable in self.__model.get_runnables:
            if runnable.is_main_runnable:
                self.__fulfill_vbox(runnable, True)
                main_counter += 1
        if main_counter > 0:
            self.__add_vertical_spacing(20)'''

        for runnable in self.__model.get_runnables:
            if not runnable.is_main_runnable:
                self.__fulfill_vbox(runnable, False)

        self.__button_widget.setLayout(self.__vbox)
        self.__scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.__scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.__scroll_area.setWidgetResizable(True)
        self.__scroll_area.setWidget(self.__button_widget)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.__scroll_area)
        self.setLayout(main_layout)
