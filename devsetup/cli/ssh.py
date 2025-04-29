from devsetup import typer, resources, run_command
from devsetup.globals import CONFIG, set_logger
from devsetup.logger import Logger

app = typer.Typer()

@app.command()
def setup(again:bool = typer.Option(False, "--again", help="never")):
    """Set up SSH"""
    set_logger(Logger())
    with resources.path("devsetup.scripts", "ssh.sh") as p:
        run_command(["bash", str(p),  CONFIG["git"]["email"], str(again)])
