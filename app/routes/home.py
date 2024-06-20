from app.constants.constants import (
    EMAIL_ME_URL,
    HEADER_ICON_BUTTONS,
    PAGES, 
    RESUME_BUTTON_NAME,
)
from app.customizations.customizable_constants import (
    EMAIL,
    FAVICON_URL, 
    FIRST_TIME_VISIT_COOKIE_EXPIRES_AFTER,
    GOOGLE_CLOUD_STORAGE_URL_START,
    NAME,
    SHORT_NAME,
    PROFILE_PIC_URL,
    RESUME_URL,
)
from flask import (
    Flask, Blueprint, make_response, request, 
    redirect, render_template, url_for
)
from app.functions.repos import (
    get_repos_from_db, 
    get_repos_from_db_filtered_by_topics,
    get_highlighted_repos_from_db
)
from app.functions.forms import create_new_form
from app.functions.database import update_database

bp = Blueprint('home', __name__, url_prefix='/')
app = Flask(__name__)


DEFAULT_VARS = {
    'EMAIL': EMAIL,
    'EMAIL_ME_URL': EMAIL_ME_URL,
    'FAVICON_URL': FAVICON_URL,
    'GOOGLE_CLOUD_STORAGE_URL_START': GOOGLE_CLOUD_STORAGE_URL_START,
    'HEADER_ICON_BUTTONS': HEADER_ICON_BUTTONS,
    'NAME': NAME,
    'SHORT_NAME': SHORT_NAME,
    'PAGES': PAGES, 
    'PROFILE_PIC_URL': PROFILE_PIC_URL,
    'RESUME_BUTTON_NAME': RESUME_BUTTON_NAME,
    'RESUME_URL': RESUME_URL,
    'request': request
}

@bp.route('/', methods=["GET", "POST"])
@bp.route('/more', methods=["GET", "POST"])
@bp.route('/highlights', methods=["GET", "POST"])
def index():
    # if users's first time visiting, 
    # set cookie & redirect to refresh route (which updates the database & re-GETs data from Github)
    if not request.cookies.get('has_visited'):
        update_database()
        response = make_response(redirect(url_for('home.refresh')))
        response.set_cookie('has_visited', 'False', max_age=FIRST_TIME_VISIT_COOKIE_EXPIRES_AFTER)
        return response
    
    # get 'topic' tags from query params
    topics = request.args.getlist('topic')
    repos = get_repos(topics, request.path)
    form = create_new_form()

    # if user submits the topic filters form, redirect to show only repos they filtered for 
    if form.validate_on_submit():
        return redirect(get_route(form.filters.data))
    
    # if the filter form was not submitted & route is '/', render the home template 
    if request.path == '/':
        return render_template('home.html', repos=repos, form=form, path=url_for('home.index'), **DEFAULT_VARS)
    # otherwise, render the repos template
    else:
        return render_template('repos.html', repos=repos, form=form, path=url_for('home.index'), **DEFAULT_VARS)


@bp.route('/refresh')
def refresh():
    update_database()
    return redirect (url_for('home.index'))


@bp.errorhandler(404)
def page_not_found(error):
    form = create_new_form()
    return render_template('error.html', form=form, title=f'Error', error=error)


# --------------
# HELPERS
# --------------
def get_repos(topics, path):
    if len(topics) == 0 and path == '/highlights': 
        return get_highlighted_repos_from_db()
    if len(topics) == 0 and path == '/more':
        return get_repos_from_db()
    else: 
        return get_repos_from_db_filtered_by_topics(topics)


def get_route(topics):
    if topics[0] == '':
        return '/more'
    else:
        topic_strings = map(lambda topic: f'topic={topic}', topics)
        return '/more?' + ('&').join(topic_strings)
