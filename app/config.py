from os import environ
from dotenv import load_dotenv

load_dotenv()

class Configuration:
    # ------------------------------------------------------------------
    # This code must be un-commented to use Heroku PostgreSQL database
    URI = environ.get('DATABASE_URL')

    if URI.startswith("postgres://"):
        URI = URI.replace("postgres://", "postgresql://", 1)
    # ------------------------------------------------------------------

    SQLALCHEMY_DATABASE_URI = URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get('SECRET_KEY')