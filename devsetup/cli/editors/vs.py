
from devsetup.cli.editors.base_editor import BaseEditor
from devsetup.cli.editors.registry_editor import register_editor

@register_editor("vs")
class VsCode(BaseEditor):
    def get_script(self):
        return "vs.sh"

