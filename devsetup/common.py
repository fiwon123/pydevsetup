import typer
import subprocess
from importlib import resources

def run_command(command: list):
    """Run a system command"""
    subprocess.run(command, check=True)