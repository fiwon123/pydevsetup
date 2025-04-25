from devsetup.cli.editors.base_editor import BaseEditor

EDITORS:dict[str, BaseEditor] = {}

# Always import class on __init__.py to be automatically register
def register_editor(name:str)->BaseEditor:
    def decorator(cls: BaseEditor):
        EDITORS[name.lower()] = cls
        return cls
    return decorator

def get_editor(name:str)->BaseEditor:
    editor_class = EDITORS.get(name.lower())
    return editor_class