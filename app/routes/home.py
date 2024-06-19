from app.constants.constants import (
    FILTERS,
    FIRST_TIME_VISIT_COOKIE_EXPIRES_AFTER,
    RESUME_BUTTON_NAME,
    GOOGLE_CLOUD_CONSOLE_BUCKET_NAME,
    HEADER_ICON_BUTTONS,
    PAGES, 
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
from app.forms.FilterReposForm import FilterReposForm
from dotenv import load_dotenv
from app.functions.repos import add_repos_to_db, update_repo,get_repos_from_github_and_add_to_db
from app.seeders.projects_without_repos import PROJECTS_WITHOUT_REPOS
from app.seeders.added_props_for_existing_repos import ADDED_PROPS_FOR_EXISTING_REPOS
from app import db

load_dotenv()

bp = Blueprint('home', __name__, url_prefix='/')
app = Flask(__name__)

DEFAULT_VARS = {
    'GOOGLE_CLOUD_CONSOLE_BUCKET_NAME': GOOGLE_CLOUD_CONSOLE_BUCKET_NAME,
    'HEADER_ICON_BUTTONS': HEADER_ICON_BUTTONS,
    'RESUME_BUTTON_NAME': RESUME_BUTTON_NAME,
    'PAGES': PAGES, 
    'request': request
}

@bp.route('/')
def index():
    # if user's first time visiting, update the database & set session cookie 
    if not request.cookies.get('first_visit'):
        update_database()
        resp = make_response(redirect(url_for('home.refresh')))
        resp.set_cookie('first_visit', 'yes', max_age=FIRST_TIME_VISIT_COOKIE_EXPIRES_AFTER)
        return resp
    return render_template("home.html", **DEFAULT_VARS)


@bp.route('/highlights')
def highlights():
    repos = get_highlighted_repos_from_db()
    return render_template("highlights.html",  repos=repos, **DEFAULT_VARS)


@bp.route('/more')
@bp.route('/more/', methods=["GET", "POST"])
def more():
    # get topics to filter by from query parameters
    topics = request.args.getlist('topic')
    # if there are filters in the query params, only get repos filtered by these topics
    if len(topics) > 0:
        repos = get_repos_from_db_filtered_by_topics(topics)
    # otherwise, get all repos
    else: 
        repos = get_repos_from_db()

    form = create_new_form()
    if form.validate_on_submit():
        route = get_route_from_filters(form.filters.data)
        return redirect(route)
    return render_template('more.html', repos=repos, form=form, path=url_for('home.more'), **DEFAULT_VARS)


@bp.route('/refresh')
def refresh():
    update_database()
    return redirect (url_for('home.index'))


@bp.errorhandler(404)
def page_not_found(error):
    form = create_new_form()
    return render_template('error.html', form=form, title=f'Error', error=error)


# ----------------
# HELPERS
# ----------------
def create_new_form():
    form = FilterReposForm()
    get_form_choices(form)
    return form


def update_database():
    # drop existing database & recreate it 
    db.drop_all()
    db.create_all()

    # add projects without repos to database
    add_repos_to_db(PROJECTS_WITHOUT_REPOS)
    
    # get repos from github & add to database
    get_repos_from_github_and_add_to_db()

    # add additional props for existing repos
    repo_names = list(ADDED_PROPS_FOR_EXISTING_REPOS.keys())

    for repo_name in repo_names:
        thumbnail_and_video_filenames = {
            'thumbnail_filename': f'{repo_name}.png',
            'video_filename': f'{repo_name}.mp4'
        }
        props_to_add = {**thumbnail_and_video_filenames, **ADDED_PROPS_FOR_EXISTING_REPOS[repo_name]}
        update_repo(repo_name, props_to_add)


def get_route_from_filters(filters):
    if (filters[0] == ''):
        return '/more'
    else: 
        return'/more?' + ('&').join(f'topic={filter}' for filter in filters )


def get_form_choices(form):
    for field in form._fields.keys():
        field = form[field].name
        type = form[field].type
        if (type == 'SelectMultipleField'):
            options = FILTERS.items()
            form[field].choices = [(value, key) for (key, value) in options]
