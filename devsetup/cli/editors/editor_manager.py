from devsetup import typer
from devsetup.cli.editors.registry_editor import get_editor
from devsetup.globals import set_logger
from devsetup.logger import Logger
from devsetup.utils import print_error, print_msg

app = typer.Typer()

@app.command()
def setup():
    set_logger(Logger())

    print_msg("Choose an editor:")
    print_msg("1 - VS Code")
    print_msg("2 - IntelliJ")
    print_msg("3 - Rider")
    print_msg("4 - Visual Studio")
    ans = input("Your option: ")

    if ans == "1":
        name = "vscode"
    elif ans == "2":
        name = "intellij"
    elif ans == "3":
        name = "rider"
    elif ans == "4":
        name = "vs"
    else:
        print_error("Choose options typing the number 1, 2, ...")

    class_reference = get_editor(name)

    if class_reference == None:
        return

    editor = class_reference()
    editor.setup()
    