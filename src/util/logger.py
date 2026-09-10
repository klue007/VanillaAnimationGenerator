from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, msg: str, color: str = ""):
        pass

    @abstractmethod
    def log_info(self, msg: str):
        pass
    
    @abstractmethod
    def log_warn(self, msg: str):
        pass
    
    @abstractmethod
    def log_success(self, msg: str):
        pass
    
    @abstractmethod
    def log_error(self, msg: str):
        pass

    @abstractmethod
    def set_progress(self, process: float):
        pass