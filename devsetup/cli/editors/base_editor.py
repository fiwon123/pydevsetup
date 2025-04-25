from devsetup import resources, run_command
from abc import ABC, abstractmethod

class BaseEditor(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_path(self):
        pass

    @abstractmethod
    def get_script(self):
        pass

    def setup(self):
        with resources.path(self.get_path(), self.get_script()) as p:
            run_command(["bash", str(p)])