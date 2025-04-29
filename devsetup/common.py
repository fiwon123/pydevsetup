import os
import platform
from shutil import which
import typer
import subprocess
from importlib import resources
from devsetup.globals import CONFIG


def run_command(command: list):
    """Run a system command"""
    if platform.system() == "Windows":
        
        # GIT Bash
        git_bash = CONFIG["common"]["git_bash"]
        if not git_bash:
            raise RuntimeError("Could not find Git Bash; please install Git for Windows.")
        # Pass the script path directly to Git Bash
        subprocess.run([git_bash] + command[1:], check=True)
    else:
        # macOS/Linux
        subprocess.run(command, check=True)