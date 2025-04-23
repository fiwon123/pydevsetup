from devsetup import typer, resources, run_command

app = typer.Typer()

@app.command()
def setup():
    """Set up editor preferences"""
    with resources.path("devsetup.scripts", "setup_editor.sh") as p:
        run_command(["bash", str(p)])