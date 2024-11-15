# TODO: Implement the add_found_runnables(searched_runnables: List) method. After searching, the found ones should be
#  added to the screen first, then the main runnables.
# TODO: Implement the add_search_bar() method. The search bar and a search button should be added to the screen.
# TODO: Add the __search() function, that calls the model's search_runnables() method.


from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from typing import List
from PyQt5.QtWidgets import QDialog

from src.model.fileinfo import FileInfo
from src.model.model import Model
from src.view.runnable_config_screen import RunnableConfigScreen
# from src.view.style.normal_text_label import NormalTextLabel
from src.view.style.normal_text_button import NormalTextButton


class ShowRunnablesScreen(QDialog):
    """
    A class that handles the UI for showing runnables.
    Attributes:
        __model (Model): The model that contains the data.
        __widget (QtWidgets.QStackedWidget): The widget that contains the screen.
        __scroll_area (QtWidgets.QScrollArea): The scroll area that contains the runnables.
        __vbox (QtWidgets.QVBoxLayout): The vertical layout that contains the runnables.
    Methods:
        __init__(model: Model, widget: QtWidgets.QStackedWidget): Initializes the ShowRunnablesScreen object with the model and widget.
        __init_ui(searched_runnables: list): Initializes the UI with the searched runnables.
        add_found_runnables(searched_runnables: list): Adds the found runnables to the UI.
    """

    def __init__(self, model: Model, widget: QtWidgets.QStackedWidget, working_dir_path: str = '',
                 searched_runnables: List = None) -> None:
        """
        Initializes the ShowRunnablesScreen object with the model and widget.
        Args:
            model (Model): The model that contains the data.
            widget (QtWidgets.QStackedWidget): The widget that contains the screen.
        """
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

    def ___init_ui(self, searched_runnables: List = None) -> None:
        """
        Initializes the UI with the searched runnables.
        Args:
            searched_runnables (list): The list of searched runnables.
        """
        self.__scroll_area = QtWidgets.QScrollArea()
        self.__button_widget = QtWidgets.QWidget()
        self.__vbox = QtWidgets.QVBoxLayout()

        self.__add_working_dir_input()
        self.__add_vertical_spacing(20)

        self.__add_clear_history_button()
        """
        search bar field
        """

        """
        favourite runnables field
        """
        try:
            self.__model.load_main()
        except:
            pass
        if len(self.__model.get_main_runnables()) > 0:
            for runnable in self.__model.get_main_runnables():
                self.__fulfill_vbox(runnable, True)
            self.__add_vertical_spacing(20)

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

    def __add_working_dir_input(self):
        """
        Adds the working directory input to the screen.
        This adds a horizontal box layout with a text edit and a button.
        The button is connected to the __try_load_show_runnables_screen method
        with the text of the text edit as the argument.
        """
        input_horizontal_box = QtWidgets.QHBoxLayout()
        input_line_edit = QtWidgets.QLineEdit(self.__model.get_working_directory_path)
        button = NormalTextButton('Change working directory')
        button.setMaximumWidth(400)
        input_horizontal_box.addWidget(input_line_edit)
        input_horizontal_box.addWidget(button)
        self.__vbox.addLayout(input_horizontal_box)
        button.clicked.connect(
            lambda _, path=self.__vbox.itemAt(0).itemAt(0).widget().text(): self.__try_load_show_runnables_screen(path)
        )

    def __fulfill_vbox(self, runnable: FileInfo, is_main: bool = False):
        """
        Adds a runnable to the vertical box layout.
        Adds a horizontal box layout to the vertical box layout with a
        button for the given runnable. The button is connected to the
        `__try_load_runnable` method with the given runnable as the argument.
        If the runnable is a favourite, the button is on the left side,
        otherwise it is on the right side.
        Args:
            runnable (FileInfo): The runnable to add to the vertical box layout.
            is_main (bool, optional): If the runnable is a favourite, by default False
        """
        horizontal_box = QtWidgets.QHBoxLayout()
        button = NormalTextButton(text=runnable.get_prog_path)
        button.clicked.connect(
            lambda _, current_runnable=runnable: self.__try_load_runnable(current_runnable)
        )
        horizontal_box.addWidget(button)

        button = NormalTextButton()
        if is_main:
            button.setText('Undo pin')
            button.clicked.connect(
                lambda _, current_runnable=runnable: self.__unset_main(current_runnable)
            )
        else:
            button.setText('Pin as favourite')
            button.clicked.connect(
                lambda _, current_runnable=runnable: self.__set_main(current_runnable)
            )
        horizontal_box.addWidget(button)
        button.setMaximumWidth(400)
        self.__vbox.addLayout(horizontal_box)

    def __add_vertical_spacing(self, space_gap: int) -> None:
        """
        Adds vertical spacing to the layout.
        This method inserts a vertical space of the given gap size
        into the vertical box layout, creating a separation between
        elements in the UI.
        Args:
            space_gap (int): The size of the space to be added, in pixels.
        """
        self.__vbox.addSpacing(space_gap)

    def __try_load_show_runnables_screen(self, working_dir_path: str = '', searched_runnables: List = None) -> None:
        """
        Attempts to load and display the ShowRunnablesScreen.
        This method initializes a ShowRunnablesScreen with the given working directory path
        and the list of searched runnables. The screen is added to the widget stack and
        displayed. If an error occurs during the process, it is silently ignored.
        Args:
            working_dir_path (str, optional): The path to the working directory, by default an empty string.
            searched_runnables (List, optional): The list of runnables to be searched and displayed, by default None.
        """
        try:
            show_runnables_screen = ShowRunnablesScreen(self.__model, self.__widget,
                                                        self.__vbox.itemAt(0).itemAt(0).widget().text(),
                                                        searched_runnables)
            self.__widget.addWidget(show_runnables_screen)
            self.__widget.setCurrentIndex(self.__widget.currentIndex() + 1)
        except:
            self.__show_message('An error occurred. Please try again.')

    def __try_load_runnable(self, runnable: FileInfo) -> None:
        """
        Attempts to load and display a RunnableConfigScreen for the given runnable.
        This method initializes a RunnableConfigScreen with the given runnable and
        adds it to the widget stack. The screen is displayed. If an error occurs
        during the process, it is silently ignored.
        Args:
            runnable (FileInfo): The runnable to be displayed.
        Returns:
            None
        """

        runnable_config_screen = RunnableConfigScreen(self.__model, runnable, self.__widget)
        self.__widget.addWidget(runnable_config_screen)
        self.__widget.setCurrentIndex(self.__widget.currentIndex() + 1)

    def __set_main(self, runnable: FileInfo) -> None:
        """
        Sets the given runnable as the main runnable.
        This method sets the given runnable as the main runnable in the model.
        Args:
            runnable (FileInfo): The runnable to be set as the main runnable.
        Returns:
            None
        """
        self.__model.set_runnable_main_property(runnable, True)
        self.__try_load_show_runnables_screen()

    def __unset_main(self, runnable: FileInfo) -> None:
        """
        Unsets the given runnable as the main runnable.
        This method unsets the given runnable as the main runnable in the model.
        Args:
            runnable (FileInfo): The runnable to be unset as the main runnable.
        Returns:
            None
        """
        self.__model.set_runnable_main_property(runnable, False)
        self.__try_load_show_runnables_screen()

    def __add_clear_history_button(self) -> None:
        """
        Adds a button to clear the history.
        This method adds a button to the vertical box layout that
        clears the history. The button is connected to the
        `__clear_history` method.
        Returns:
            None
        """
        button = NormalTextButton(text='Clear history')
        button.clicked.connect(self.__clear_history)
        self.__vbox.addWidget(button)
        self.__add_vertical_spacing(20)

    def __clear_history(self):
        """
        Clears the history and refreshes the screen.

        This method clears the history in the model and refreshes the screen
        by calling `__try_load_show_runnables_screen`.
        """
        self.__model.clear_history()
        self.__try_load_show_runnables_screen()

    def __add_search_bar(self) -> None:
        """
        Adds a search bar to the vertical box layout.

        This method adds a horizontal box layout with a text edit and two buttons
        to the vertical box layout. The first button is for searching and the second
        button is for clearing the search. The buttons are connected to the
        `__search` and `__clear_search` methods, respectively. The text edit is also
        connected to the `__search` method, so that the search is triggered when the
        user presses Enter.

        Returns:
            None
        """
        self.__add_vertical_spacing(20)
        horizontal_box = QtWidgets.QHBoxLayout()
        search_button = NormalTextButton(text='Search', tool_tip='Search for runnables')
        search_line_edit = NormalTextLineEdit()
        search_line_edit.returnPressed.connect(search_button.click)
        search_button.clicked.connect(self.__search)
        horizontal_box.addWidget(search_line_edit)
        horizontal_box.addWidget(search_button)
        search_button = NormalTextButton(text='Clear', tool_tip='Clear search')
        search_button.clicked.connect(self.__clear_search)
        horizontal_box.addWidget(search_button)
        self.__vbox.addLayout(horizontal_box)
        self.__add_vertical_spacing(20)

    def __search(self) -> None:
        """
        Searches for runnables in the model with the given text.

        This method takes the text from the search bar, searches the model for
        runnables with the given text, and refreshes the screen with the found
        runnables. If no runnables are found, it shows an error message.

        Returns:
            None
        """
        searched_runnables = self.__model.search_runnable(
            self.__vbox.itemAt(4).layout().itemAt(0).widget().text().strip())
        if (not searched_runnables) or searched_runnables == []:
            self.__show_message('No runnables found. Please try again.')
        else:
            self.__try_load_show_runnables_screen(searched_runnables=searched_runnables)

    def __clear_search(self) -> None:
        """
        Clears the search bar and refreshes the screen.

        This method clears the search bar, clears the history in the model, and
        refreshes the screen by calling `__try_load_show_runnables_screen`. If an
        error occurs, it shows an error message.

        Returns:
            None
        """
        try:
            self.__model.clear_history()
            self.__try_load_show_runnables_screen()
        except:
            self.__show_message('An error occurred. Please try again.')

    def __add_found_runnables(self, searched_runnables: List = None) -> None:
        if searched_runnables:
            inner_box = QtWidgets.QVBoxLayout()
            for runnable in searched_runnables:
                button = NormalTextButton(text=runnable.get_prog_path)
                button.clicked.connect(lambda _, current_runnable=runnable: self.__try_load_runnable(current_runnable))
                inner_box.addWidget(button)
            self.__vbox.addLayout(inner_box)
            self.__add_vertical_spacing(20)

    @staticmethod
    def __show_message(message: str) -> None:
        """
        Displays a message box with the given message.
        This static method creates and displays a QMessageBox
        with the provided message text. The message box is
        executed modally, blocking the rest of the application
        until it is closed.
        Args:
            message (str): The message to be displayed in the message box.
        Returns:
            None
        """
        msg = QtWidgets.QMessageBox()
        msg.setText(message)
        msg.exec_()
