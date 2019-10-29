from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class FindForm(FlaskForm):
    build = StringField('Build', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    # remember_me = BooleanField('Remember me')
    submit = SubmitField('Find')
