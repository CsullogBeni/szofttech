from src.persistence.idata_access import IDataAccess
import os
import json


class DataAccess(IDataAccess):
    """
    A class that handles data persistence for the application.

    Attributes:
        __app_data_path (str): The path to users AppData local directory.

    Methods:
        __init__(data_path: str): Initializes the DataAccess object with the application data path.
        save_config(runnable: str, data: dict): Saves the configuration for a runnable.
        load_config(runnable: str) -> dict: Loads the configuration for a runnable.
        save_main_runnables(data: dict): Saves the main runnables.
        load_main_runnables() -> dict: Loads the main runnables.
        clear_history(): Clears the configuration history.
    """

    def __init__(self) -> None:
        self.__app_data_path = os.path.join(os.environ['LOCALAPPDATA'], "SZOFTECH")

    def save_config(self, runnable: str, data: dict) -> None:
        """
        Saves the configuration for a runnable.

        Args:
            runnable (str): The name of the runnable.
            data (dict): The configuration data.
        """
        self.__check_or_create_app_data_dir()

        file_name = runnable.replace('/', '_').replace('\\', '_') + ".json"
        file_path = os.path.join(self.__app_data_path, file_name)

        with open(file_path, 'w') as json_file:
            json.dump(data, json_file)

    def load_config(self, runnable: str) -> dict:
        """
        Loads the configuration for a runnable.

        Args:
            runnable (str): The name of the runnable.

        Returns:
            dict: The configuration data.

        Raises:
            FileNotFoundError: If the configuration file is not found.
        """
        file_name = runnable.replace('/', '_').replace('\\', '_') + ".json"
        file_path = os.path.join(self.__app_data_path, file_name)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No configuration file found for {runnable}")
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        return data

    def save_main_runnables(self, data: dict) -> None:
        """
        Saves the main runnables.

        Args:
            data (dict): The main runnables data.
        """
        self.__check_or_create_app_data_dir()

        file_path = os.path.join(self.__app_data_path, "main_runnables.json")

        with open(file_path, 'w') as json_file:
            json.dump(data, json_file)

    def load_main_runnables(self) -> dict:
        """
        Loads the main runnables.

        Returns:
            dict: The main runnables data.

        Raises:
            FileNotFoundError: If the main runnables file is not found.
        """
        file_path = os.path.join(self.__app_data_path, "main_runnables.json")
        if not os.path.exists(file_path):
            raise FileNotFoundError("No main runnables configuration file found")
        with open(file_path, 'r') as json_file:
            main_runnables = json.load(json_file)

        return main_runnables

    def clear_history(self) -> None:
        """
        Clears the configuration history.
        """
        for filename in os.listdir(self.__app_data_path):
            file_path = os.path.join(self.__app_data_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

    def __check_or_create_app_data_dir(self) -> None:
        """
        This function check whether AppData local directory exists at __app_data_path,
        and if it doesn't, it will be created.
        """
        if not os.path.exists(self.__app_data_path):
            os.makedirs(self.__app_data_path, exist_ok=True)

    def save_working_directory_path(self, full_path: str) -> None:
        """
        This function saves the given path as the Model's working directory path into a json file in App Data Directory

        Args:
            full_path: the path to save as the Model's working directory path

        """
        data_to_save = dict()
        data_to_save['working_directory_path'] = full_path

        self.__check_or_create_app_data_dir()

        file_path = os.path.join(self.__app_data_path, 'working_dir_path.json')

        with open(file_path, 'w') as json_file:
            json.dump(data_to_save, json_file)

    def load_working_directory_path(self) -> str | None:
        """
        This function loads the Model's working directory path from working_dir_path.json file in App Data Directory

        Returns:
            str | None: the loaded path, if it has been saved previously, or None if it hasn't
        """
        file_path = os.path.join(self.__app_data_path, 'working_dir_path.json')

        if not os.path.exists(file_path):
            return None

        with open(file_path, 'r') as json_file:
            file_data = json.load(json_file)

            return file_data['working_directory_path']
