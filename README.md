# 💬 About

A simple command-line to configure dev workflow.

## ✨ Features


## 🚀 Installation
```bash
pip install .
```

For development:
```bash
pip install -e .
```

## 🛠 Usage
Use this following command to formmat any file available in the package:
```bash
devtool
```

Use this command to list all availables parameters:
```bash
devtool --help
```


## 📁 Project Structure
```text
devtool-project/
├── devtool/                  # Main package
│   ├──__init__.py
│   ├──__main__.py
│   ├── cli.py
│   ├── editor_setup.ssh
│   ├── git_config.ssh
│   └── ssh_setup.ssh
├── LICENSE     
├── CHANGELOG.md
├── README.md
└── pyproject.toml            # Project metadata
```


## 🧪 Running Tests
```bash
pytest
```

## 🧾 License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.