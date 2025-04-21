from devsetup import typer, resources, subprocess, run_command

app = typer.Typer()

@app.command()
def editor():
    """Set up editor preferences"""
    with resources.path("devsetup", "scripts/editor_setup.sh") as p:
        run_command(["bash", str(p)])