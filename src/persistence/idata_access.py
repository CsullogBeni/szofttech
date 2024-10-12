# TODO: Create IDAtaAccess interface that contains the following abstract methods:
#  - save_config(runnable: FileInfo, data: dict) -> None
#  - load_config(runnable: FileInfo) -> dict
#  - save_main_runnables(runnables: data: dict) -> None
#  - load_main_runnables() -> dict
#  - clear_history() -> None

from abc import ABC, abstractmethod
class IDataAccess(ABC):
    @abstractmethod
    def save_config(runnable: str, data: dict):
        pass
    @abstractmethod
    def load_config(runnable: str) -> dict:
        pass
    @abstractmethod
    def save_main_runnables(runnables: dict):
        pass
    @abstractmethod
    def load_main_runnables() -> dict:
        pass
    @abstractmethod
    def clear_history():
        pass
    
    