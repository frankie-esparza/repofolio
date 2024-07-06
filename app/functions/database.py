from app.customizations.add_projects_without_repos import PROJECTS_WITHOUT_REPOS
from app.customizations.add_priority_and_highlight import REPOS_WITH_PRIORITY_OR_HIGHLIGHT
from app.customizations.settings import (
    FILE_TYPE_FOR_IMAGES, FILE_TYPE_FOR_VIDEOS
)
from app.customizations.add_videos_and_thumbnails import REPOS_WITH_THUMBNAILS, REPOS_WITH_VIDEOS 

from app.functions.repos import add_repos_to_db, update_repo,get_repos_from_github_and_add_to_db
from app.functions.repos import get_repos_from_github_and_add_to_db
from app import db


def update_database():    
    get_repos_from_github_and_add_to_db()

    add_repos_to_db(PROJECTS_WITHOUT_REPOS)

    for (repo, props) in REPOS_WITH_PRIORITY_OR_HIGHLIGHT.items():
        update_repo(repo, props)

    for repo in REPOS_WITH_THUMBNAILS:
        props = {
            'thumbnail_filename': f'{repo}{FILE_TYPE_FOR_IMAGES}',
        }
        update_repo(repo, props)

    for repo in REPOS_WITH_VIDEOS:
        props = {
            'video_filename': f'{repo}{FILE_TYPE_FOR_VIDEOS}'
        }
        update_repo(repo, props)


    