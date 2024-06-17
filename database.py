from dotenv import load_dotenv
from app.functions.repos import add_repos_to_db, update_repo, get_repo_by_name, get_repos_from_github_and_add_to_db
from app.seeders.projects_without_repos import PROJECTS_WITHOUT_REPOS
from app.seeders.added_props_for_existing_repos import ADDED_PROPS_FOR_EXISTING_REPOS
load_dotenv()

from app import app, db

with app.app_context():
    # drop existing database & recreate it 
    db.drop_all()
    db.create_all()

    # add projects without repos to database
    add_repos_to_db(PROJECTS_WITHOUT_REPOS)

    # get repos from github & add to database
    get_repos_from_github_and_add_to_db()

    # add additional props for existing repos (priority ranking & video links)
    repo_names = list(ADDED_PROPS_FOR_EXISTING_REPOS.keys())
    for repo_name in repo_names:
        update_repo(repo_name, ADDED_PROPS_FOR_EXISTING_REPOS[repo_name])

            
            

