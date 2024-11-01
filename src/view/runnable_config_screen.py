import re

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from src.model.argument import Argument
from src.model.fileinfo import FileInfo
from src.model.model import Model
from src.view.runner_screen import RunnerScreen
from src.view.style.normal_text_button import NormalTextButton
from src.view.style.normal_text_label import NormalTextLabel

'''from src.view.style.title_text_label import TitleTextLabel
from src.view.style.normal_text_line_edit import NormalTextLineEdit
from src.view.style.normal_text_combobox import NormalTextComboBox'''


# TODO: Implement the __equip_button_action(button: QtButton) method. This should add aa button to the screen.

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
        __vbox:        The QVBoxLayout widget of the screen
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
        self.__show_main_buttons()

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
        # runnable_path = TitleTextLabel(self.__get_dark_blue_label_text("Fullpath: ") + self.__runnable.get_prog_path)
        runnable_path = NormalTextLabel(self.__get_dark_blue_label_text("Fullpath: ") + self.__runnable.get_prog_path)
        runnable_path.setMaximumWidth(1100)
        self.__vbox.addWidget(runnable_path)
        if self.__runnable.get_prog_name:
            runnable_prog = NormalTextLabel(
                self.__get_dark_blue_label_text("Program: ") + self.__runnable.get_prog_name)
            runnable_prog.setMaximumWidth(1100)
            self.__vbox.addWidget(runnable_prog)
        if self.__runnable.get_prog_description:
            '''description = self.split_argument_label_info(self.__runnable.get_prog_description)
            runnable_desc = NormalTextLabel(self.__get_dark_blue_label_text("Program's description: ") + description)
            runnable_desc.setMaximumWidth(1100)
            self.__vbox.addWidget(runnable_desc)'''
        self.__add_vertical_spacing()
        self.__show_prog_args(clear)

    def __show_prog_args(self, clear: bool) -> None:
        """
        This method shows the arguments of the runnable which has to be executed.
        Args:
            clear: This parameter decides whether the configuration of the given runnable has to be loaded.

        Returns:
            None
        """
        for arg in self.__runnable.get_args:
            arg_description = f"Argument: {arg.get_id}"
            if arg.get_second_id:
                arg_description += f" / {arg.get_second_id}, "
            else:
                arg_description += ", "
            if arg.get_default is not None:
                arg_description += f"Default: {arg.get_default}, "
            if arg.get_help:
                arg_description += f"Help: {arg.get_help}, "
            if arg.get_type:
                arg_description += f"Type: {arg.get_type}, "
            if arg.get_required:
                arg_description += f"Required: {arg.get_required}, "
            if arg.get_action:
                arg_description += f"Action: {arg.get_action}, "
            arg_description = self.__split_argument_label_info(arg_description)
            arg_description = self.__add_arg_desc_style(arg_description)
            widget = NormalTextLabel(arg_description)
            widget.setMaximumWidth(1100)
            self.__vbox.addWidget(widget)
            self.__add_input_field(arg)
        if not clear:
            self.__load_config()

    def __show_main_buttons(self) -> None:
        """
        This method initialize the main buttons of the screen.
        Returns:
            None
        """
        button = NormalTextButton('Clear history')
        button.clicked.connect(self.__clear_args)
        self.__vbox.addWidget(button)
        button = NormalTextButton('Run')
        button.clicked.connect(self.__run_configuration)
        self.__vbox.addWidget(button)
        button = NormalTextButton('Back')
        button.clicked.connect(self.__go_to_show_runnables_screen)
        self.__vbox.addWidget(button)

        self.__button_widget.setLayout(self.__vbox)

    def __add_vertical_spacing(self, space_gap: int = 33) -> None:
        """
        This method adds vertical spacing to the layout.
        Args:
            space_gap: The size of the space to be added, in pixels.

        Returns:
            None
        """
        spacer = QtWidgets.QSpacerItem(0, space_gap, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.__vbox.addItem(spacer)

    def __run_configuration(self) -> None:
        """
        This method creates the command string from the input fields and initialize a new RunnerScreen.
        Returns:
            None
        """
        command = self.__runnable.get_prog_path
        current_arg = None
        for widget_idx in range(self.__vbox.count()):
            widget = self.__vbox.itemAt(widget_idx).widget()
            layout = self.__vbox.itemAt(widget_idx).layout()
            if isinstance(widget, NormalTextLabel):
                current_arg = self.extract_argument(self.remove_text_in_angle_brackets(widget.text()))
            elif (isinstance(layout, QtWidgets.QHBoxLayout)
                  and isinstance(layout.itemAt(1).widget(), QtWidgets.QLineEdit)):
                # and isinstance(layout.itemAt(1).widget(), NormalTextLineEdit)):
                input_from_widget = layout.itemAt(1).widget().text().strip()
                if not current_arg:
                    return
                elif not input_from_widget or current_arg == input_from_widget:
                    continue
                elif current_arg in input_from_widget:
                    command = command + ' ' + input_from_widget
                else:
                    command = command + ' ' + current_arg + ' ' + input_from_widget
        try:
            runner_screen = RunnerScreen(self.__model, self.__widget, self.__runnable, command)
            self.__widget.addWidget(runner_screen)
            self.__widget.setCurrentIndex(self.__widget.currentIndex() + 1)
        except Exception as e:
            self.__show_message_box(f'Error while running runnable\n{e}', 'Error')
        self.__save_config()

    def __go_to_show_runnables_screen(self) -> None:
        """
        This method initialize a new ShowRunnablesScreen and tries to go to it. Moreover, it saves the configuration.
        Returns:
            None
        """
        from src.view.show_runnables_screen import ShowRunnablesScreen
        try:
            show_runnables_screen = ShowRunnablesScreen(self.__model, self.__widget,
                                                        self.__model.get_working_directory_path)
            self.__widget.addWidget(show_runnables_screen)
            self.__widget.setCurrentIndex(self.__widget.currentIndex() + 1)
        except Exception as e:
            self.__show_message_box(f'Failed to go to the screen os runnables. Reason: {e}', 'Error')
        self.__save_config()

    @staticmethod
    def __show_message_box(text: str, window_title: str = None):
        """
        Shows a message box.
        Args:
            text: message box text
            window_title: message box title
        """
        msg_box = QtWidgets.QMessageBox()
        msg_box.setText(text)
        if window_title is not None:
            msg_box.setWindowTitle(window_title)
        msg_box.exec()

    @staticmethod
    def __split_argument_label_info(arg_description: str) -> str:
        """
        This method splits the description to fit on the screen.
        Args:
            arg_description: Description to display

        Returns:
            str: The modified description
        """
        arg_info = arg_description.split(' ')
        arg_description = ''
        chars_in_one_line = 0
        for arg_member in arg_info:
            if chars_in_one_line + len(arg_member) < 110:
                arg_description = arg_description + ' ' + arg_member
                chars_in_one_line = chars_in_one_line + len(arg_member)
            else:
                arg_description = arg_description + '<br>' + arg_member
                chars_in_one_line = len(arg_member)
        return arg_description.strip()

    @staticmethod
    def extract_argument(text: str) -> None or str:
        """
        This method filters the argument name from the argument's detail.
        Args:
            text: the argument's detail

        Returns:
            None or str: the filtered argument, or None if it doesn't exist
        """
        try:
            start = text.find('Argument: ') + len('Argument: ')
            end = text.find(' /', start)
            if end == -1:
                end = text.find(',', start)
            if start == -1 or end == -1:
                return None
            return text[start:end]
        except:
            return None

    @staticmethod
    def remove_text_in_angle_brackets(text: str) -> str:
        """
        This method removes the angle brackets from the given text.
        Usually xml/html codes are located between angle brackets.
        Args:
            text: the text from which square brackets are removed

        Returns:
            str: the modified text
        """
        pattern = r"<.*?>"
        return re.sub(pattern, "", text)

    @staticmethod
    def __add_arg_desc_style(arg_description: str) -> str:
        """
        This method adds style to the string (similar like html).
        Args:
            arg_description: the text to format

        Returns:
            str: the styled text
        """
        if arg_description.endswith(', '):
            arg_description = arg_description[:-2]
        if arg_description.endswith(','):
            arg_description = arg_description[:-1]
        arg_description = "<p style=\"font-size:16px;\">" + arg_description + "</p>"
        keywords = ['Argument:', 'Default:', 'Help:', 'Type:', 'Required:', 'Action:']
        for word in keywords:
            arg_description = arg_description.replace(word, RunnableConfigScreen.__get_dark_blue_label_text(word))
        return arg_description

    def __add_input_field(self, arg: Argument) -> None:
        """
        This method adds an input field to the screen for the given argument.
        Args:
            arg: argument to which the input field will be given

        Returns:
            None
        """
        hbox = QtWidgets.QHBoxLayout()
        arg_flag = NormalTextLabel(arg.get_id + ': ')
        if len(arg_flag.text()) < 100:
            arg_flag.setMaximumWidth(150)
        hbox.addWidget(arg_flag)
        # hbox.addWidget(NormalTextLineEdit(default_text=arg.get_id, arg_default=arg.get_default))
        hbox.addWidget(QtWidgets.QLineEdit())
        self.__vbox.addLayout(hbox)
        self.__add_vertical_spacing()

        self.__add_vertical_spacing()

    def __clear_args(self):
        """
        This method clears all the input fields and initialize a new RunnableConfigScreen with the same runnable.
        """
        runnable_screen = RunnableConfigScreen(self.__model, self.__runnable, self.__widget, True)
        self.__widget.addWidget(runnable_screen)
        self.__widget.setCurrentIndex(self.__widget.currentIndex() + 1)

    def __save_config(self):
        """
        This method saves the arguments of the runnable in the model.
        It iterates over the widgets in the vertical box layout.
        If the widget is a horizontal box layout with a line edit or a combo box, it adds the text of the line edit or
        the current text of the combo box to the arguments list.
        If the widget is a button, it adds True to the arguments list if the button's text is 'Equipped', otherwise it
        adds False. Finally, it calls the save_config method of the model with the runnable and the arguments list.
        """
        args = []
        for widget_idx in range(self.__vbox.count()):
            if isinstance(self.__vbox.itemAt(widget_idx).layout(), QtWidgets.QHBoxLayout):
                # if isinstance(self.__vbox.itemAt(widget_idx).layout().itemAt(1).widget(), NormalTextLineEdit):
                if isinstance(self.__vbox.itemAt(widget_idx).layout().itemAt(1).widget(), QtWidgets.QLineEdit):
                    args.append(self.__vbox.itemAt(widget_idx).layout().itemAt(1).widget().text().strip())
                # elif isinstance(self.__vbox.itemAt(widget_idx).layout().itemAt(1).widget(), NormalTextComboBox):
                elif isinstance(self.__vbox.itemAt(widget_idx).layout().itemAt(1).widget(), QtWidgets.QComboBox):
                    args.append(self.__vbox.itemAt(widget_idx).layout().itemAt(1).widget().currentText().strip())
            elif isinstance(self.__vbox.itemAt(widget_idx).widget(), NormalTextButton):
                if self.__vbox.itemAt(widget_idx).widget().text() == 'Equipped':
                    args.append(True)
                else:
                    args.append(False)
        self.__model.save_config(self.__runnable, args)

    def __load_config(self):
        """
        This method loads the saved configuration for the runnable.
        It iterates over the widgets in the vertical box layout.
        If the widget is a horizontal box layout with a line edit or a combo box, it sets the text of the line edit or
        the current text of the combo box from the saved configuration.
        If the widget is a button, it sets the text of the button to 'Equipped' or 'Equip' based on the saved
        configuration.
        """
        current_config = self.__model.load_config(self.__runnable)
        if current_config == {}:
            return
        current_args = current_config['args']
        for widget_idx in range(self.__vbox.count()):
            if isinstance(self.__vbox.itemAt(widget_idx).layout(), QtWidgets.QHBoxLayout):
                # if isinstance(self.__vbox.itemAt(widget_idx).layout().itemAt(1).widget(), NormalTextLineEdit):
                if isinstance(self.__vbox.itemAt(widget_idx).layout().itemAt(1).widget(), QtWidgets.QLineEdit):
                    self.__vbox.itemAt(widget_idx).layout().itemAt(1).widget().setText(current_args[0])
                    current_args = self.__list_reducer(current_args)
                # elif isinstance(self.__vbox.itemAt(widget_idx).layout().itemAt(1).widget(), NormalTextComboBox):
                elif isinstance(self.__vbox.itemAt(widget_idx).layout().itemAt(1).widget(), QtWidgets.QComboBox):
                    self.__vbox.itemAt(widget_idx).layout().itemAt(1).widget().setCurrentText(current_args[0])
                    current_args = self.__list_reducer(current_args)
            elif isinstance(self.__vbox.itemAt(widget_idx).widget(), NormalTextButton):
                if current_args[0]:
                    self.__vbox.itemAt(widget_idx).widget().setText('Equipped')
                    # still nem tudom, hogy jo e
                    self.__vbox.itemAt(widget_idx).widget().setStyleSheet("background-color: green")
                else:
                    self.__vbox.itemAt(widget_idx).widget().setText('Equip')
                    self.__vbox.itemAt(widget_idx).widget().setStyleSheet("background-color: red")
                current_args = self.__list_reducer(current_args)

