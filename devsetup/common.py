import os
import platform
from shutil import which
import typer
import subprocess
from importlib import resources
from devsetup.globals import CONFIG

def find_git_bash() -> str | None:
    return CONFIG["common"]["git_bash"]


    # First see if "bash.exe" on PATH is actually Git Bash
    path = which("bash.exe")
    if path and "Git" in path:
        return path
    # Otherwise try the usual Git install locations
    for root in [os.getenv("ProgramFiles"), os.getenv("ProgramFiles(x86)")]:
        if root:
            candidate = os.path.join(root, "Git", "bin", "bash.exe")
            if os.path.isfile(candidate):
                return candidate
    return None

def run_command(command: list):
    """Run a system command"""
    if platform.system() == "Windows":
        
        # Try to find Git Bash or fall back to WSL
        git_bash = find_git_bash()
        print(git_bash)
        if not git_bash:
            raise RuntimeError("Could not find Git Bash; please install Git for Windows.")
        # Pass the script path directly to Git Bash
        subprocess.run([git_bash] + command[1:], check=True)
    else:
        # macOS/Linux
        subprocess.run(command, check=True)