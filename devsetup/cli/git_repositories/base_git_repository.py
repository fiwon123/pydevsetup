from abc import ABC, abstractmethod
from devsetup import typer, resources, run_command
from devsetup.globals import CONFIG
from devsetup.utils import print_msg

class BaseGitRepository(ABC):
    def __init__(self):
        super().__init__()

    def get_path(self):
        return "devsetup.scripts.git_repositories"

    @abstractmethod
    def get_script(self):
        pass
        
    def setup(self):
        print_msg("Type your git repository name: ")
        repository_name = input("name: ")

        with resources.path(self.get_path(), self.get_script()) as p:
            run_command(["bash", str(p), CONFIG["git"]["username"], repository_name])