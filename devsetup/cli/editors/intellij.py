from devsetup.cli.editors.base_editor import BaseEditor
from devsetup.cli.editors.registry_editor import register_editor

@register_editor("intellij")
class VsCode(BaseEditor):
    def get_script(self):
        return "intellij.sh"

