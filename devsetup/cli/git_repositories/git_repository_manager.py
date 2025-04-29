from importlib import resources
from devsetup import typer
from devsetup.cli.git_repositories.registry_git_repository import get_git_repository
from devsetup.common import run_command
from devsetup.globals import CONFIG, set_logger
from devsetup.logger import Logger
from devsetup.utils import print_error, print_msg

app = typer.Typer()

@app.command()
def init():
    set_logger(Logger())

    with resources.path("devsetup.scripts", "git.sh") as p:
        run_command(["bash", str(p), CONFIG["git"]["username"], CONFIG["git"]["email"]])


@app.command()
def setup():
    set_logger(Logger())

    print_msg("Choose a git repository:")
    print_msg("1 - Gihub")
    print_msg("2 - Gitlab")
    ans = input("Your option: ")

    if ans == "1":
        name = "github"
    elif ans == "2":
        name = "gitlab"
    else:
        print_error("Choose options typing the number 1, 2, ...")

    class_reference = get_git_repository(name)

    if class_reference == None:
        return

    git_repository = class_reference()
    git_repository.setup()