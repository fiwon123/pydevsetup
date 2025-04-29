from devsetup import typer
from devsetup.cli.editors.registry_editor import get_editor
from devsetup.globals import set_logger
from devsetup.logger import Logger

app = typer.Typer()

@app.command()
def setup(name: str = typer.Option(..., "--name", "-n", help="Editor name in lowercase. (vscode, intellij, rider, vs ...)")):
    set_logger(Logger())
    class_reference = get_editor(name)

    if class_reference == None:
        return

    editor = class_reference()
    editor.setup()
    