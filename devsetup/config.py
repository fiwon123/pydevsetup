from pathlib import Path
import tomllib  # Python 3.11+

from devsetup.utils import get_platform_home_path, join_paths, path_exists

def load_config():
    file_path = get_platform_home_path()
    file_path = join_paths(file_path, "devsetup/config.toml")

    if not path_exists(file_path):
        return
        # raise FileNotFoundError(f"No config file found: {file_path}")
    
    with Path.open(file_path, "rb") as f:
        return tomllib.load(f)