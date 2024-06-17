from app.constants.constants import (
    PAGES, 
    GOOGLE_CLOUD_CONSOLE_BUCKET_NAME,
    HEADER_ICON_BUTTONS,
    FIRST_TIME_VISIT_COOKIE_EXPIRES_AFTER
)
from flask import (
    Flask, Blueprint, make_response, request, 
    redirect, render_template, url_for
)
from app.functions.repos import (
    delete_repos_from_db,
    get_repos_from_db, 
    get_repos_from_github_and_add_to_db, 
    get_repos_from_db_filtered_by_topics,
    get_highlighted_repos_from_db
)

bp = Blueprint('home', __name__, url_prefix='/')
app = Flask(__name__)

DEFAULT_VARS = {
    'GOOGLE_CLOUD_CONSOLE_BUCKET_NAME': GOOGLE_CLOUD_CONSOLE_BUCKET_NAME,
    'HEADER_ICON_BUTTONS': HEADER_ICON_BUTTONS,
    'PAGES': PAGES, 
    'request': request
}

@bp.route('/')
def index():
    return render_template("home.html", **DEFAULT_VARS)


@bp.route('/highlights')
def highlights():
    repos = get_highlighted_repos_from_db()
    return render_template("repos.html", repos=repos, **DEFAULT_VARS)


@bp.route('/more')
@bp.route('/more/')
def projects():
    # if user's first time visiting, get repos from github & refresh database
    if not request.cookies.get('first_visit'):
        resp = make_response(redirect(url_for('home.refresh')))
        resp.set_cookie('first_visit', 'yes', max_age=FIRST_TIME_VISIT_COOKIE_EXPIRES_AFTER)
        return resp
    else:
        # get topics to filter by from query parameters
        topics = request.args.getlist('topic')
        if len(topics) > 0:
            repos = get_repos_from_db_filtered_by_topics(topics)
        # if there are no filters, just get repos from db
        else: 
            repos = get_repos_from_db()
    return render_template('repos.html', repos= repos, **DEFAULT_VARS)



@bp.route('/refresh')
def refresh():
    repos = get_repos_from_db()
    delete_repos_from_db(repos)
    get_repos_from_github_and_add_to_db()
    return redirect(url_for('home.index'))


@bp.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', title=f'Error', error=error)