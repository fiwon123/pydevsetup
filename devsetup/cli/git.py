from devsetup import typer, resources, run_command
from devsetup.globals import CONFIG

app = typer.Typer()

@app.command()
def setup(is_repository:bool = typer.Option(False, "-repo", "--repository", help="Configure reposutiry to use SSH.")):
    """Set up Git"""
    if is_repository:
        with resources.path("devsetup.scripts", "setup_git_repository.sh") as p:
            run_command(["bash", str(p), CONFIG["git"]["ssh_repository"]])
    else:
        with resources.path("devsetup.scripts", "setup_git.sh") as p:
            run_command(["bash", str(p), CONFIG["git"]["user_name"], CONFIG["git"]["user_email"]])