from devsetup.cli.git_repositories.base_git_repository import BaseGitRepository


GIT_REPOSITORIES: dict[str, BaseGitRepository] = {}

def register_git_repository(name:str)->BaseGitRepository:
    def decorator(class_name:BaseGitRepository):
        GIT_REPOSITORIES[name.lower()] = class_name
        return class_name
    return decorator

def get_git_repository(name:str)->BaseGitRepository:
    return GIT_REPOSITORIES.get(name.lower())