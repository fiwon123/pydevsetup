from devsetup import typer
from devsetup.cli.editors.registry_editor import get_editor

app = typer.Typer()

@app.command()
def setup(name: str = typer.Option(..., "--name", "-n", help="Editor name in lowercase. (vscode, intellij, rider, vs ...)")):
    editor_class = get_editor(name)

    editor = editor_class()
    editor.setup()
    