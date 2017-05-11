from flask import Flask
from .pathfinder import path_finder
from flask import render_template, flash
from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from app import app
from .forms import LoginForm, InputForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = InputForm()
    # res = path_finder('lest-west', '314')
    # flash('Login requested for OpenID="%s"' % form.openid.data)
    start = form.start.data
    finish = form.finish.data
    # tmp = path_finder(form.openid.data, '314')
    # tmp = path_finder('301', '323')
    tmp = 0
    if start and finish:
        tmp = path_finder(start, finish)
    return render_template('index.html',
                           title='nav',
                           form=form,
                           start=start,
                           finish=finish,
                           tmp=tmp)
