from app.customizations.settings import GITHUB_USERNAME, MAX_REPOS_IN_GET_QUERY
from app.models import PROPS_NOT_IN_GITHUB_RESPONSE
from app.models import db, Repo
import requests
import json 

def get_all_repos_from_db():
    return (
        db.session.execute(
            db.select(Repo)
            .order_by(Repo.priority)
            .filter(Repo.html_url != None)
        ).scalars().all()
    )


def get_highlighted_repos_from_db():
    return (
         db.session.execute(
            db.select(Repo).filter_by(highlighted=True)
            .order_by(Repo.priority)
        ).scalars()
    )

def get_all_repos_from_db_filtered_by_topics(topics):
    return (
        db.session.execute(
            db.select(Repo)
            .filter(Repo.html_url != None)
            .filter(Repo.topics.overlap(topics))
            .order_by(Repo.priority)
        ).scalars()
    )


def get_repos_from_github_and_add_to_db():
    repos = get_repos_from_github()
    repos_filtered = filter_out_unused_props_from_github(repos)
    add_repos_to_db(repos_filtered)


def add_repos_to_db(repos):
    try:
        for repo in repos:
            repo_in_database = get_repo_by_name(repo['name'])
            if not repo_in_database:
                new_repo = Repo(**repo)
                db.session.add(new_repo)
                db.session.commit()
        print('\n🎉 Added these repos to the database:\n', get_repos_string(repos) )
    except Exception as err:
        print(f'❌ Error while adding repos to the database\n', err)


def get_repos_from_github():
    url = f'https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page={MAX_REPOS_IN_GET_QUERY}'
    header = {}

    # --------------------------------------------------------------------
    # Note: If you get the "❌ Error while getting repos from Github" error
    # try: 
    # 1) Authenticating from the command line - https://docs.github.com/en/get-started/getting-started-with-git/set-up-git
    # 2) Getting a "personal access token" from github - https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
    # 3) Add the GITHUB_ACCESS_TOKEN to your .env file
    # 3) Uncomment the lines below 
    # 
    # token = os.getenv('GITHUB_ACCESS_TOKEN')
    # header =  { 'Authorization': f'Bearer {token}' }
    # ----------------------------------------------------------------------
    try:
        res = requests.get(url, header)
        res.raise_for_status()  # Raise an exception for HTTP errors
        repos = json.loads(res.text)
        print('\n🎉 Got these repos from Github:\n', get_repos_string(repos))
        return repos 
    except Exception as err: 
        print(f'\n❌ Error while getting repos from Github.\n', err)


# ----------------------
# HELPERS
# ----------------------
def get_repos_string(repos):
    return (', ').join(list(map(lambda repo: repo['name'], repos)))


def delete_repos_from_db(repos):
    for repo in repos:
        repo = get_repo_by_id(repo.id)
        db.session.delete(repo)
        db.session.commit()


def get_repo_by_id(id):
    return (
        db.session.execute(
            db.select(Repo).filter_by(id=id)
        ).scalar_one_or_none()
    )


def get_repo_by_name(name):
    return (
        db.session.execute(
            db.select(Repo).filter_by(name=name)
        ).scalar_one_or_none()
    )

def update_repo(repo_name, new_props):
    repo = get_repo_by_name(repo_name)
    for key, value in new_props.items():
         setattr(repo, key, value)
    db.session.commit()



def filter_out_unused_props_from_github(repos):
    # get array of props desired based on the Repo model
    keys = get_github_keys(Repo)
    filtered_repos = []

    for repo in repos:
        # map each repo to an object with only the desired key/value pairs
        values = map(lambda key: repo[key], keys)
        new_repo = dict(zip(keys, values))
        filtered_repos.append(new_repo)
    return filtered_repos


def get_github_keys(model):
    model_props = [column.name for column in model.__table__.columns]
    github_props = list(filter(lambda key: key not in PROPS_NOT_IN_GITHUB_RESPONSE, model_props))
    return github_props