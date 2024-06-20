from app.forms.FilterReposForm import FilterReposForm
from app.customizations.filters import FILTERS


def create_new_form():
    form = FilterReposForm()
    get_form_choices(form)
    return form


def get_form_choices(form):
    for field in form._fields.keys():
        field = form[field].name
        type = form[field].type
        if (type == 'SelectMultipleField'):
            options = FILTERS.items()
            form[field].choices = [(value, key) for (key, value) in options]
