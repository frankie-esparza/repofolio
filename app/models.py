from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY

PROPS_NOT_IN_GITHUB_RESPONSE = [
    'display_name',
    'priority',
    'highlighted',
    'video_filename',
    'thumbnail_filename'
]

db = SQLAlchemy()

# the Repo class represents a single project, most often associated with a particular repo in Github 
# you can also have instance of the Repo class that are not associated with projects in Github 
# (see comments in /customizations/add_projects_without_repos.py)
class Repo(db.Model):
    __tablename__ = "repos"

    # ----------------------------------------
    # Props that match Github API Response
    # ----------------------------------------
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)        # repo name 
    description = db.Column(db.String(2000), nullable=True) # description in the 'About' section of the repo
    stargazers_count = db.Column(db.Integer, nullable=True) # stars received on the repo
    language = db.Column(db.String(100), nullable=True)     # primary programming language (e.g. Python, JavaScript)
    topics=db.Column(ARRAY(db.String), nullable=True)       # 'topics' in Github, learn more here - https://docs.github.com/en/enterprise-server@3.10/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics
    html_url = db.Column(db.String(2000), nullable=True)    # url for the repo 
    homepage = db.Column(db.String(2000), nullable=True)    # website for the demo of the project  

    # --------------------------------------------
    # Props that DO NOT match Github API Response
    # --------------------------------------------
    display_name = db.Column(db.String(100), nullable=True)       # use this prop if you want some other name that's different from the repo name on the page
    priority = db.Column(db.Integer, nullable=True)               # Sets the order on which the repo shows up on the page
    highlighted = db.Column(db.Boolean, nullable=True)            # If true, repo will show up on the "Highlights" page
    video_filename = db.Column(db.String(100), nullable=True)     # filename for the video
    thumbnail_filename = db.Column(db.String(100), nullable=True) # filename for the image 

