from app.functions.repos import add_repos_to_db, update_repo, get_repo_by_name, get_repos_from_github_and_add_to_db
from app.customizations.projects_without_repos import PROJECTS_WITHOUT_REPOS
from app.customizations.added_props_for_existing_repos import ADDED_PROPS_FOR_EXISTING_REPOS
from app import app, db
from app.functions.database import update_database

# drop all tables in existing database & recreate 
with app.app_context():
    update_database()
            
            

