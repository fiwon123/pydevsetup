from devsetup import typer, resources, run_command
from devsetup.globals import CONFIG

app = typer.Typer()

@app.command()
def setup(again:bool = typer.Option(False, "--again", help="never")):
    """Set up SSH"""
    with resources.path("devsetup.scripts", "setup_ssh.sh") as p:
        run_command(["bash", str(p),  CONFIG["git"]["user_email"], str(again)])
