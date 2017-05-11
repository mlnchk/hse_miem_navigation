from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])


class InputForm(Form):
    start = StringField('start', validators=[DataRequired()])
    finish = StringField('finish', validators=[DataRequired()])