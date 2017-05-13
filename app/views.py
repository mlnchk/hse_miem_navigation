from flask import Flask
from .pathfinder import shortest_path
from flask import render_template
from app import app
from .forms import LoginForm, InputForm

graph = {
    'LW': {'301', '325', '401', '425'},
    'LN': {'307', '308', '317', '407', '408', '417'},
    'LS': {'Lu', '317', '308', '417', '408'},
    'LE': {'LE', '312', '313', '412', '413'},
    'Lu': {'LS', 'Lu', '315', '308', '415', '408'},
    'WC3': {'317', '321'},
    '301': {'LW', '302', '325'},
    '302': {'301', '303', '325'},
    '303': {'302', '304', '324'},
    '304': {'303', '305', '323'},
    '305': {'304', '306', '321'},
    '306': {'305', '307', 'WC3'},
    '307': {'306', 'LN', 'WC3'},
    '308': {'LN', '309', 'LS', 'Lu'},
    '309': {'308', '310', '315'},
    '310': {'309', '311', '314'},
    '311': {'310', '312', '314'},
    '312': {'311', 'LE'},
    '313': {'314', 'LE'},
    '315': {'Lu', '309'},
    '314': {'313', '315', '310', '311'},
    '317': {'LS', 'LN', 'WC3'},
    '321': {'WC3', '305', '323'},
    '323': {'321', '305', '324'},
    '324': {'323', '325', '303'},
    '325': {'324', '302', 'LW'},
    'WC4': {'417', '421'},
    '401': {'LW', '402', '425'},
    '402': {'401', '403', '425'},
    '403': {'402', '404', '424'},
    '404': {'403', '405', '423'},
    '405': {'404', '406', '421'},
    '406': {'405', '407', 'WC4'},
    '407': {'406', 'LN', 'WC4'},
    '408': {'LN', '409', 'LS', 'Lu'},
    '409': {'408', '410', '415'},
    '410': {'409', '411', '414'},
    '411': {'410', '412', '414'},
    '412': {'411', 'LE'},
    '413': {'414', 'LE'},
    '415': {'Lu', '409'},
    '414': {'413', '415', '410', '411'},
    '417': {'LS', 'LN', 'WC4'},
    '421': {'WC4', '405', '423'},
    '423': {'421', '405', '424'},
    '424': {'423', '425', '403'},
    '425': {'424', '402', 'LW'}
}


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
        tmp = shortest_path(graph, start, finish)

    return render_template('index.html',
                           title='nav',
                           form=form,
                           start=start,
                           finish=finish,
                           tmp=tmp)
