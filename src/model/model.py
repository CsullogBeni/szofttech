# TODO: Create model class. It should contain the following private variables:
#  - __working_directory_path:  str
#  - __runnables:               List[FileInfo]
#  - __data_access:             DataAccess

# TODO: Create constructor for model class, that sets all variables above.
# TODO: Create getters for __working_directory_path, __runnables variables.
# TODO: Create add_working_directory_path() method that adds the given path to current working directory and runs through the directory recursively, searching for runnables, consider using argument_visitor.
# TODO: Create add_default_path() method that ads the current working directory to default paths.
# TODO: Create run_program(command: str) method that executes the given command.
# TODO: Creat clear_history() method that clears the history.

# TODO: Create save_config(runnable: FileInfo, args: List) method that saves the given runnable and its arguments.
# TODO: Create load_config(runnable: FileInfo) method that loads the given runnable.
# TODO: Create __filter_main_runnables() method that filters the runnables that are marked as main.
# TODO: Create set_runnable_main_property(runnable: FileInfo, currently_mian: Bool) method that sets the main property of the given runnable.

# TODO: Create search_runnables(given_string: str) method that searches the given_string in __runnables and __main_runnables.
# TODO: Implement the searching algorithm in __searching_algorithm(given_string: str, runnables: List).
