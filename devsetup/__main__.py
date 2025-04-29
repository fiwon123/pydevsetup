import os
from pathlib import Path
import platform
from devsetup import typer
from devsetup.cli import ssh
from devsetup.cli.editors import editor_manager
from devsetup.cli.git_repositories import git_repository_manager
from devsetup.logger import Logger
from devsetup.utils import copy_from_to, create_dir, join_paths, path_exists, print_msg
from devsetup.globals import set_logger

app = typer.Typer()

# Registering subcommands (modular CLI)
app.add_typer(git_repository_manager.app, name="git")
app.add_typer(ssh.app, name="ssh")
app.add_typer(editor_manager.app, name="editor")

@app.command()
def init():
    set_logger(Logger())

    if platform.system() == "Windows":
        path = join_paths(os.getenv("LOCALAPPDATA"), "devsetup")
        create_dir(path)
    elif platform.system() == "Darwin":
        path = join_paths(Path.home(), "Library/devsetup")
    elif platform.system() == "Linux":
        path = join_paths(Path.home(), ".config/devsetup")

    create_dir(path)

    path = join_paths(path, "config.toml")
    if path_exists(path):
        print_msg("File config.toml already exists!")
    else:
        print_msg("Do you want create a sample config.toml? (Y/N)")
        ans = input()
        if (ans.upper() == "Y"):
            copy_from_to("devsetup/config_sample.toml",path)
    


if __name__ == "__main__":
    app()