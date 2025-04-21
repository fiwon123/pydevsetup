from devsetup import typer, resources, subprocess, run_command

app = typer.Typer()

@app.command()
def git():
    """Configure Git"""
    with resources.path("devsetup", "scripts/git_config.sh") as p:
        run_command(["bash", str(p)])