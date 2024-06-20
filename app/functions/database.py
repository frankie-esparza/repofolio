from app.customizations.projects_without_repos import PROJECTS_WITHOUT_REPOS
from app.customizations.added_props_for_existing_repos import ADDED_PROPS_FOR_EXISTING_REPOS
from app.functions.repos import add_repos_to_db, update_repo,get_repos_from_github_and_add_to_db
from app.functions.repos import get_repos_from_github_and_add_to_db
from app import db


def update_database():
    # drop existing database & recreate it 
    db.drop_all()
    db.create_all()

    # add projects without repos to database
    add_repos_to_db(PROJECTS_WITHOUT_REPOS)
    
    # get repos from github & add to database
    get_repos_from_github_and_add_to_db()

    # add additional props for existing repos
    repo_names = list(ADDED_PROPS_FOR_EXISTING_REPOS.keys())

    for repo_name in repo_names:
        thumbnail_and_video_filenames = {}
        # if repo is highlighted, add links for the thumbnail & video 
        if ADDED_PROPS_FOR_EXISTING_REPOS[repo_name].get('highlighted'): 
            thumbnail_and_video_filenames = {
                'thumbnail_filename': f'{repo_name}.png',
                'video_filename': f'{repo_name}.mp4'
            }
        # update repo with additional props
        props_to_add = {**thumbnail_and_video_filenames, **ADDED_PROPS_FOR_EXISTING_REPOS[repo_name]}
        update_repo(repo_name, props_to_add)