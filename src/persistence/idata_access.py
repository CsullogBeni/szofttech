from abc import ABC, abstractmethod


class IDataAccess(ABC):
    """
    Abstract class for data access classes.

    The classes that implement this interface should provide methods for saving and loading
    configurations of the runnable programs and the list of main runnables.
    """

    @abstractmethod
    def save_config(self, runnable: str, data: dict):
        pass

    @abstractmethod
    def load_config(self, runnable: str) -> dict:
        pass

    @abstractmethod
    def save_main_runnables(self, runnables: dict):
        pass

    @abstractmethod
    def load_main_runnables(self) -> dict:
        pass

    @abstractmethod
    def clear_history(self):
        pass

    @abstractmethod
    def save_working_directory_path(self, full_path: str) -> None:
        pass

    @abstractmethod
    def load_working_directory_path(self) -> str | None:
        pass
