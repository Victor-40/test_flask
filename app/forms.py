from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired


class FindForm(FlaskForm):
    build = StringField('Build', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    # remember_me = BooleanField('Remember me')
    submit = SubmitField('Find')


class RadioForm(FlaskForm):
    rf = RadioField()
    submit = SubmitField('Go-Go')


class SelSetup(FlaskForm):
    sf = SelectField()
    submit = SubmitField('Select')
