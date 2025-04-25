from devsetup import typer
from devsetup.cli import ssh
from devsetup.cli.editors import editor_manager
from devsetup.cli.git_repositories import git_repository_manager
from devsetup.config import load_config

app = typer.Typer()

# Registering subcommands (modular CLI)
app.add_typer(git_repository_manager.app, name="git")
app.add_typer(ssh.app, name="ssh")
app.add_typer(editor_manager.app, name="editor")

if __name__ == "__main__":
    app()