from app import app, db
from app.functions.database import update_database

with app.app_context():
    # drops all existing tables in the database
    db.drop_all()

    # re-creates all tables
    db.create_all()

    # GETs repos from Github & seeds database with additional projects & properties from '/customizations' 
    update_database()