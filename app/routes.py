from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import FindForm, RadioForm, SelSetup
from app import utils

setups = list()

@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Victor"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/find_builds', methods=['GET', 'POST'])
def find_builds():
    form = FindForm()
    global setups
    if form.validate_on_submit():
        setups = utils.find_builds(form.build.data, form.tag.data)
        setups_count = len(setups)

        return render_template('result.html', title='result', form=form, setups=setups, setups_count=setups_count)
        # flash("Find build {}, tag {}".format(form.build.data, form.tag.data))
    setups = list()
    return render_template('find_builds.html', title='Find', form=form)


@app.route('/make_xls')
def make_xls():
    res = utils.make_xls(setups)
    count = len(res)
    return render_template('make_xls.html', title='xls', res=res, count=count )


@app.route('/single_setup', methods=['GET', 'POST'])
def single_setup():
    form = RadioForm()
    user = {'username': "Victor"}
    form.rf.label = "Choose product"
    lst = [('CFW', 'CFW'),
           ('EFD.LAB', 'EFD.LAB'),
           ('EFD.NX', 'EFD.NX'),
           ('EFD.PRO', 'EFD.PRO'),
           ('EFD.SE', 'EFD.SE'),
           ('EFD.V5', 'EFD.V5')]
    form.rf.choices = lst

    if form.validate_on_submit():
        # print("sf", form1.sf.data)
        # print("rf", form.rf.data)

        return redirect(url_for('test'), code=303)
    else:
        return render_template('single_setup.html', title='Home', user=user, form=form)


@app.route('/test', methods=['GET', 'POST'])
def test():
    user = {'username': "Victor"}
    lst = [('CFW', 'CFW'),
           ('EFD.LAB', 'EFD.LAB'),
           ('EFD.NX', 'EFD.NX'),
           ('EFD.PRO', 'EFD.PRO'),
           ('EFD.SE', 'EFD.SE'),
           ('EFD.V5', 'EFD.V5')]
    form = SelSetup()
    form.sf.choices = lst
    form.sf.label = "Choose setup"
    if form.validate_on_submit():
        print("sf", form.sf.data)

        return render_template('test_1.html', user=user, form=form)
    else:
        return render_template('test_1.html', title='Home', user=user, form=form)