import os
from pathlib import Path
import platform
import shutil
import typer
from rich.console import Console
from rich.panel import Panel
import devsetup.globals

console = Console()

def print_error(msg: str):
    typer.echo(f"❌ [ERROR] {msg}", err=True)
    devsetup.globals.get_logger().save_log(f"[ERROR] {msg}")
    raise typer.Exit(1)

def print_warning(msg: str):
    typer.echo(f"⚠️  [WARNING] {msg}")
    devsetup.globals.get_logger().save_log(f"[WARNING] {msg}")

def print_msg(msg: str, enable_icon: bool = False):
    if enable_icon:
        typer.echo(f"✅ {msg}")
    else:
        typer.echo(msg)

    devsetup.globals.get_logger().save_log(msg)

def error_box(message: str):
    console.print(Panel(message, title="[red]Error[/red]", border_style="red"))

def get_extension(filepath: str):
    return os.path.splitext(filepath)[1]

def get_dir_path(filepath: str):
    return os.path.dirname(filepath)

def get_file_name(filepath: str):
    return os.path.splitext(os.path.basename(filepath))[0]

def create_dir(filepath: str):
    if not os.path.exists(filepath):
        os.makedirs(filepath)

def get_path(path: str):
    return Path(path)

def join_paths(base_path: str, sub_path: str):
    return os.path.join(base_path, sub_path)

def path_exists(filepath: str):
    if os.path.exists(filepath):
        return True
    
    return False

def copy_from_to(src, dest):
    shutil.copyfile(src, dest)

def get_platform_home_path():
    path = ""
    if platform.system() == "Windows":
        path = os.getenv("LOCALAPPDATA")
        create_dir(path)
    elif platform.system() == "Darwin":
        path = join_paths(Path.home(), "Library")
    elif platform.system() == "Linux":
        path = join_paths(Path.home(), ".config")

    return path