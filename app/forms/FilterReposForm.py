from flask_wtf import FlaskForm;
from wtforms import SubmitField, SelectMultipleField
from wtforms.validators import DataRequired

default = [DataRequired()]

class FilterReposForm(FlaskForm):
    filters = SelectMultipleField('', validators=default, render_kw={'class': 'select-multiple-field'})
    submit = SubmitField('Apply Filters')