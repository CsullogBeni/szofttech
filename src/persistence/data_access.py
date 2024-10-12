from idata_access import IDataAccess
import os, json


class DataAccess(IDataAccess):
    """
    Implements IDataAccess interface, provides methods for saving and loading configurations of runnables, and saving and loading the main runnables' configuration.

    Attributes:
        __app_data_path (str): The path to the directory where the configuration files are stored.

    Methods:
        __init__(data_path: str): Initializes the DataAccess object with the given data path.
        save_config(runnable: str, data: dict): Saves the given data as a json file in the SZOFTECH directory under the given runnable's name.
        load_config(runnable: str) -> dict: Loads the configuration for the given runnable from a json file in the SZOFTECH directory under the given runnable's name.
        save_main_runnables(data: dict): Saves the given data as a json file in the SZOFTECH directory under the name 'main_runnables.json'.
        load_main_runnables() -> dict: Loads the main runnables' configuration from a json file in the SZOFTECH directory under the name 'main_runnables.json'.
        clear_history(): Clears the history of the main runnables by deleting all the files in the SZOFTECH directory.
    """
    def __init__(self,data_path: str):
        self.__app_data_path = data_path

    def save_config(self,runnable: str, data: dict):
        """
        Saves the given data as a json file in the SZOFTECH directory under the given runnable's name.

        :param runnable: The name of the runnable
        :param data: The data to be saved
        :return: None
        """
        config_dir = os.path.join(self.__app_data_path, "SZOFTECH")
        if not os.path.exists(config_dir):
            os.makedirs(config_dir,exist_ok=True)
        file_name = f"{runnable}.json"
        file_path = os.path.join(config_dir, file_name)
        
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
    def load_config(self, runnable: str) -> dict:
        """
        Loads the configuration for the given runnable from a json file in the SZOFTECH directory under the given runnable's name.

        :Args:
            runnable: The name of the runnable
        :Returns
            The loaded data as a dictionary
        :Raises
            FileNotFoundError: If no configuration file is found for the given runnable
        """
        file_name = f"{runnable}.json" 
        file_path = os.path.join(self.__app_data_path, "SZOFTECH", file_name)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No configuration file found for {runnable}")
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
        return data
    
    def save_main_runnables(self, data: dict):
        """
        Saves the given data as a json file in the SZOFTECH directory under the name 'main_runnables.json'.
        The data is filtered to include only the main runnables.

        :Args:
            data: The data to be saved
        :Returns
            None
        """
        main_runnables = {key: value for key, value in data.items() if value}
        config_dir = os.path.join(self.__app_data_path, "SZOFTECH")
        if not os.path.exists(config_dir):
            os.makedirs(config_dir, exist_ok=True)

        file_path = os.path.join(config_dir, "main_runnables.json")

        with open(file_path, 'w') as json_file:
            json.dump(main_runnables, json_file, indent=4, default=lambda o: o.__dict__)

    def load_main_runnables(self) -> dict:
        """
        Loads the main runnables' configuration from a json file in the SZOFTECH directory under the name 'main_runnables.json'.
        The configuration is a dictionary where the keys are the names of the runnables and the values are the runnables' data.

        :Returns
            The loaded main runnables configuration as a dictionary
        :Raises
            FileNotFoundError: If no main runnables configuration file is found
        """
        file_path = os.path.join(self.__app_data_path, "SZOFTECH", "main_runnables.json")
        if not os.path.exists(file_path):
            raise FileNotFoundError("No main runnables configuration file found")
        with open(file_path, 'r') as json_file:
            main_runnables = json.load(json_file)
        
        return main_runnables

    def clear_history(self):
        """
        Clears the history of the main runnables by deleting all the files in the SZOFTECH directory.
        """
        config_dir = os.path.join(self.__app_data_path, "SZOFTECH")
        for filename in os.listdir(config_dir):
            file_path = os.path.join(config_dir, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
