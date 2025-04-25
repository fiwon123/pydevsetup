
from devsetup.cli.editors.base_editor import BaseEditor
from devsetup.cli.editors.registry_editor import register_editor

@register_editor("vscode")
class VsCode(BaseEditor):
    def get_path(self):
        return "devsetup.scripts.editors"

    def get_script(self):
        return "vscode.sh"

