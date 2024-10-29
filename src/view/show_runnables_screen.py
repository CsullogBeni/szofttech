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


