from devsetup import typer
from devsetup.cli import git, ssh, editor

app = typer.Typer()

# Registering subcommands (modular CLI)
app.add_typer(git.app, name="git")
app.add_typer(ssh.app, name="ssh")
app.add_typer(editor.app, name="editor")

if __name__ == "__main__":
    app()