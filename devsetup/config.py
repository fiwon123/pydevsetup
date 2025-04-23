import tomllib  # Python 3.11+
from pathlib import Path

def load_config():
    config_path = Path("devsetup_config.toml")
    if not config_path.exists():
        raise FileNotFoundError("No config file found: devsetup_config.toml")
    
    with config_path.open("rb") as f:
        return tomllib.load(f)