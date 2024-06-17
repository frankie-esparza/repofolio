from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY

PROPS_NOT_IN_GITHUB_RESPONSE = [
    'display_name',
    'priority',
    'highlighted',
    'video_filename',
    'thumbnail_filepath'
]

db = SQLAlchemy()

# For code simplicty, props match the props in the response of the Gihub API
class Repo(db.Model):
    __tablename__ = "repos"

    # ----------------------------------------
    # Props that match Github API Response
    # ----------------------------------------
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(2000), nullable=True)
    stargazers_count = db.Column(db.Integer, nullable=True)
    language = db.Column(db.String(100), nullable=True)
    topics=db.Column(ARRAY(db.String), nullable=True)
    html_url = db.Column(db.String(2000), nullable=True) # url for the repo 
    homepage = db.Column(db.String(2000), nullable=True) # website for the demo of the project  

    # --------------------------------------------
    # Props that DO NOT match Github API Response
    # --------------------------------------------
    display_name = db.Column(db.String(100), nullable=True)
    priority = db.Column(db.Integer, nullable=True)
    highlighted = db.Column(db.Boolean, nullable=True)
    video_filename = db.Column(db.String(100), nullable=True) # route for the static video
    thumbnail_filepath = db.Column(db.String(100), nullable=True) # route for the static thumbnail image

