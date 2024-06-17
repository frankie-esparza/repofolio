from app.constants.constants import GITHUB_USERNAME, MAX_REPOS_IN_GET_QUERY
from app.models import PROPS_NOT_IN_GITHUB_RESPONSE
from app.models import db, Repo
from dotenv import load_dotenv
import requests
import json 
import os 

load_dotenv()


def get_repos_from_db():
    return (
        db.session.execute(
            db.select(Repo)
            .order_by(Repo.priority)
        ).scalars().all()
    )

def get_repos_from_github_and_add_to_db():
    repos = get_repos_from_github()
    repos_filtered = filter_out_unused_props_from_github(repos)
    add_repos_to_db(repos_filtered)


def get_highlighted_repos_from_db():
    res = (
         db.session.execute(
            db.select(Repo).filter_by(highlighted=True)
            .order_by(Repo.priority)
        ).scalars()
    )
    return res


def get_repos_from_db_filtered_by_topics(topics):
    res = (
        db.session.query(Repo)
        .filter(Repo.topics.overlap(topics))
        .order_by(Repo.priority)
    )
    return res

# ----------------------
# HELPERS
# ----------------------
def delete_repos_from_db(repos):
    for repo in repos:
        repo = get_repo_by_id(repo.id)
        db.session.delete(repo)
        db.session.commit()
        print('✅ Deleted repo from db')


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


def add_repos_to_db(repos):
    for repo in repos:
        repo_in_database = get_repo_by_name(repo['name'])
        if not repo_in_database:
            new_repo = Repo(**repo)
            db.session.add(new_repo)
            db.session.commit()
    print('✅ Added repos to db')


def update_repo(repo_name, new_props):
    repo = get_repo_by_name(repo_name)
    print('REPO', repo)
    for key, value in new_props.items():
         setattr(repo, key, value)
    db.session.commit()


def get_repos_from_github():
    token = os.getenv('GITHUB_ACESS_TOKEN')
    url = f'https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page={MAX_REPOS_IN_GET_QUERY}'
    header =  { 'Authorization': f'Bearer {token}' }
    try:
        res = requests.get(url, header)
        repos = json.loads(res.text)
        print('🐯 Got repos from github')
        return repos 
    except: 
        print(f'❌ Error while getting repos.\n {res}')


def filter_out_unused_props_from_github(repos):
    # get array of props desired based on the Repo model
    keys = get_github_keys(Repo)
    filtered_repos = []

    for repo in repos:
        # map each repo to an object with only the desired key/value pairs
        values = map(lambda key: repo[key], keys)
        new_repo = dict(zip(keys, values))
        filtered_repos.append(new_repo)

    print('✅ Filtered ununsed props from github')
    return filtered_repos


def get_github_keys(model):
    model_props = [column.name for column in model.__table__.columns]
    github_props = list(filter(lambda key: key not in PROPS_NOT_IN_GITHUB_RESPONSE, model_props))
    print('GITHUB KEYS', github_props)
    return github_props