from devsetup import typer, resources, subprocess, run_command

app = typer.Typer()

@app.command()
def ssh():
    """Set up SSH"""
    with resources.path("devsetup", "scripts/ssh_setup.sh") as p:
        run_command(["bash", str(p)])
