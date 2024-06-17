from flask import Flask 
from .config import Configuration 
from .models import db
from .routes import home
from whitenoise import WhiteNoise

app = Flask(__name__)

# Get environmental variables
app.config.from_object(Configuration)

# Register Flask blueprints
app.register_blueprint(home.bp)

# Wrap app in a whitenoise object for serving static assets
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")

db.init_app(app)