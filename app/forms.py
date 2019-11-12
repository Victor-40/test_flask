from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired


class FindForm(FlaskForm):
    build = StringField('Build', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    # remember_me = BooleanField('Remember me')
    cfw = BooleanField(label="CFW", default=True)
    lab = BooleanField(label="EFD.LAB", default=True)
    nx = BooleanField(label="EFD.NX", default=True)
    pro = BooleanField(label="EFD.PRO", default=True)
    se = BooleanField(label="EFD.SE", default=True)
    v5 = BooleanField(label="EFD.V5", default=True)
    submit = SubmitField('Find')


class RadioForm(FlaskForm):
    rf = RadioField()
    pth = RadioField()
    submit = SubmitField('Select')


class RadioForm1(FlaskForm):
    rf = RadioField()
    submit = SubmitField('Select')


class SelSetup(FlaskForm):
    sf = SelectField()
    submit = SubmitField('Select')
