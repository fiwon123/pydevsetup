from devsetup.cli.git_repositories.base_git_repository import BaseGitRepository
from devsetup.cli.git_repositories.registry_git_repository import register_git_repository

@register_git_repository("gitlab")
class Gitlab(BaseGitRepository):
    def get_script(self):
        return "gitlab.sh"