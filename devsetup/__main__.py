import os
from devsetup import typer
from devsetup.cli import ssh
from devsetup.cli.editors import editor_manager
from devsetup.cli.git_repositories import git_repository_manager
from devsetup.logger import Logger
from devsetup.utils import copy_from_to, create_dir, get_platform_home_path, join_paths, path_exists, print_msg
from devsetup.globals import set_logger
import tomllib 
import toml

app = typer.Typer()

# Registering subcommands (modular CLI)
app.add_typer(git_repository_manager.app, name="git")
app.add_typer(ssh.app, name="ssh")
app.add_typer(editor_manager.app, name="editor")

@app.command()
def init(is_open:bool = typer.Option(False, "--open", help="Open folder location."),
         dry_run: bool = typer.Option(False, "--dr", help="Preview")):
    set_logger(Logger())

    path = get_platform_home_path()
    path = join_paths(path, "devsetup")
    create_dir(path)

    if (is_open):
        os.startfile(path)
        return

    path = join_paths(path, "config.toml")
    if not path_exists(path):
        print_msg("Do you want create a sample config.toml? (Y/N)")
        ans = input()
        if (ans.upper() == "Y"):
            copy_from_to("devsetup/config_sample.toml",path)
            print_msg(f"Config.toml file created: {path}")

    with open(path,'rb') as f:
        data = tomllib.load(f)

    print_msg("Do you want to edit your username? (Y/N)")
    ans = input()
    if (ans.upper() == "Y"):
        print_msg("Type your username:")
        ans = input()
        data["git"]["user_name"] = ans

    print_msg("Do you want to edit your email? (Y/N)")
    ans = input()
    if (ans.upper() == "Y"):
        print_msg("Type your email:")
        ans = input()
        data["git"]["user_email"] = ans

    if dry_run:
        print_msg("-----------")
        print_msg("Content:")
        print_msg("")
        print_msg(toml.dumps(data))
        return

    with open(path,'w') as f:
        toml.dump(data, f)
    


if __name__ == "__main__":
    app()