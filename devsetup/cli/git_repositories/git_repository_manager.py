from devsetup import typer
from devsetup.cli.git_repositories.registry_git_repository import get_git_repository

app = typer.Typer()

@app.command()
def setup(name:str = typer.Option(..., "--name", "-n", help="Git Repository name in lowercase. (github, gitlab, ...)")):
    class_reference = get_git_repository(name)

    if class_reference == None:
        return

    git_repository = class_reference()
    git_repository.setup()