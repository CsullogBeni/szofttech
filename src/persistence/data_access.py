from persistence.idata_access import IDataAccess
import os, json

"""
This module provides a class DataAccess that handles data persistence for the application.
It inherits from IDataAccess and implements the abstract methods for saving and loading configurations.
"""

from persistence.idata_access import IDataAccess
import os, json

class DataAccess(IDataAccess):
    """
    A class that handles data persistence for the application.

    Attributes:
    __app_data_path (str): The path to the application data directory.

    Methods:
    __init__(data_path: str): Initializes the DataAccess object with the application data path.
    save_config(runnable: str, data: dict): Saves the configuration for a runnable.
    load_config(runnable: str) -> dict: Loads the configuration for a runnable.
    save_main_runnables(data: dict): Saves the main runnables.
    load_main_runnables() -> dict: Loads the main runnables.
    clear_history(): Clears the configuration history.
    """

    def __init__(self, data_path: str):
        """
        Initializes the DataAccess object with the application data path.

        Args:
        data_path (str): The path to the application data directory.
        """
        self.__app_data_path = os.path.join(data_path, "SZOFTECH")

    def save_config(self, runnable: str, data: dict):
        """
        Saves the configuration for a runnable.

        Args:
        runnable (str): The name of the runnable.
        data (dict): The configuration data.
        """
        if not os.path.exists(self.__app_data_path):
            os.makedirs(self.__app_data_path, exist_ok=True)
        file_name = runnable.replace('/','_').replace('\'','_') + ".json"
        file_path = os.path.join(self.__app_data_path, file_name)
        
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
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
        file_name = runnable.replace('/','_').replace('\'','_') + ".json"
        file_path = os.path.join(self.__app_data_path, file_name)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No configuration file found for {runnable}") 
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
        return data
    
    def save_main_runnables(self, data: dict):
        """
        Saves the main runnables.

        Args:
        data (dict): The main runnables data.
        """
        if not os.path.exists(self.__app_data_path):
            os.makedirs(self.__app_data_path, exist_ok=True)

        file_path = os.path.join(self.__app_data_path, "main_runnables.json")

        with open(file_path, 'w') as json_file:
            json.dump(data)

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

    def clear_history(self):
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
