# TODO: Create Model class. It should contain the following private variables:
#  - __working_directory_path:  str
#  - __runnables:               List[FileInfo]
#  - __main_runnables:          List[FileInfo]
#  - __data_access:             DataAccess

# TODO: Create constructor for Model class, that sets all variables above.
# TODO: Create getters for __working_directory_path, __runnables, __main_runnables variables.
# TODO: Create add_default_path() method that ads the current working directory to default paths.
# TODO: Create __set_all_runnable function that unions the __runnables and __main_runnables.
# TODO: Create run_program(command: str) method that executes the given command.
# TODO: Creat clear_history() method that clears the history.

# TODO: Create save_config(runnable: FileInfo, args: List) method that saves the given runnable and its arguments.
# TODO: Create load_config(runnable: FileInfo) method that loads the given runnable.
# TODO: Create save_main_runnables() method that saves the __main_runnables.
# TODO: Create load_main_runnables() method that loads the __main_runnables.
# TODO: Create __filter_main_runnables(main_runnables: List) method that filters the __main_runnables.
# TODO: Create set_runnable_main_property(runnable: FileInfo, currently_mian: Bool) method that sets the main property of the given runnable.

# TODO: Create search_runnables(given_string: str) method that searches the given_string in __runnables and __main_runnables.
# TODO: Implement the searching algorithm in __searching_algorithm(given_string: str, runnables: List).
