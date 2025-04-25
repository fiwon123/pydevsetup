from abc import ABC, abstractmethod
from devsetup import typer, resources, run_command
from devsetup.globals import CONFIG

class BaseGitRepository(ABC):
    def __init__(self):
        super().__init__()

    def get_path(self):
        return "devsetup.scripts.git_repositories"

    @abstractmethod
    def get_script(self):
        pass
        
    def setup(self, is_repository:bool = typer.Option(False, "-repo", "--repository", help="Configure reposutiry to use SSH.")):
        if is_repository:
            with resources.path(self.get_path(), self.get_script()) as p:
                run_command(["bash", str(p), CONFIG["git"]["ssh_repository"]])
        else:
            with resources.path("devsetup.scripts", "setup_git.sh") as p:
                run_command(["bash", str(p), CONFIG["git"]["user_name"], CONFIG["git"]["user_email"]])