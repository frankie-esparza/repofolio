from app.customizations.add_projects_without_repos import PROJECTS_WITHOUT_REPOS
from app.customizations.add_priority_and_highlight import REPOS_WITH_PRIORITY_OR_HIGHLIGHT
from app.customizations.settings import (
    FILE_TYPE_FOR_IMAGES, FILE_TYPE_FOR_VIDEOS
)
from app.customizations.add_videos_and_thumbnails import REPOS_WITH_VIDEOS_OR_THUMBNAILS

from app.functions.repos import add_repos_to_db, update_repo,get_repos_from_github_and_add_to_db
from app.functions.repos import get_repos_from_github_and_add_to_db
from app import db


def update_database():    
    get_repos_from_github_and_add_to_db()

    # Add projects that don't have repos to the database
    add_repos_to_db(PROJECTS_WITHOUT_REPOS)

    # Add 'priority' & 'highlighted' props to existing repos 
    for (repo, props) in REPOS_WITH_PRIORITY_OR_HIGHLIGHT.items():
        update_repo(repo, props)

    # add 'thumbnail_filename' & 'video_filename' props to existing repos
    for repo in REPOS_WITH_VIDEOS_OR_THUMBNAILS:
        props = {
            'thumbnail_filename': f'{repo}{FILE_TYPE_FOR_IMAGES}',
            'video_filename': f'{repo}{FILE_TYPE_FOR_VIDEOS}'
        }
        update_repo(repo, props)