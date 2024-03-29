from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import FindForm, RadioForm, RadioForm1
from app import utils
import os

setups = list()
setups_d = list()


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
        prod_lst = list()
        # print('form.cfw.data: ', form.cfw.data)
        if form.cfw.data:
            prod_lst.append(form.cfw.label.text)
            # print('prod_lst: ', prod_lst)
        if form.lab.data:
            prod_lst.append(form.lab.label.text)
        if form.nx.data:
            prod_lst.append(form.nx.label.text)
        if form.pro.data:
            prod_lst.append(form.pro.label.text)
        if form.se.data:
            prod_lst.append(form.se.label.text)
        if form.v5.data:
            prod_lst.append(form.v5.label.text)

        setups = utils.find_builds(form.build.data, form.tag.data, prod_lst)
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
    global setups_d
    form = RadioForm()
    user = {'username': "Victor"}
    form.rf.label = "Choose product"
    lst_0 = ['CFW-2021', 'CFW-2020', 'EFD.LAB-2019', 'EFD.NX-2019', 'EFD.PRO-2019', 'EFD.SE-2019', 'EFD.V5-2019']
    lst = [(x, x) for x in lst_0]
    form.rf.choices = lst

    form.pth.choices = [('', '\\'), ('_Internal', '_Internal'), ('_External', '_External'), ('_Main', '_Main')]

    if form.validate_on_submit():
        p = form.pth.data
        # print('p: ', p)
        setups_d = utils.make_dir_list(form.rf.data, p)

        return redirect(url_for('test'), code=302)
    else:
        return render_template('single_setup.html', title='Home', user=user, form=form)


@app.route('/test', methods=['GET', 'POST'])
def test():
    user = {'username': "Victor"}

    form = RadioForm1()
    form.rf.choices = setups_d
    form.rf.label = "Choose setup"
    if form.validate_on_submit():
        print("form.rf.data", form.rf.data)
        # print("getattr ", getattr(g, 'data', None))

        return render_template('test.html', user=user, form=form)
    else:

        # print("setups 2 ", setups_d)
        # print(g['data'])
        return render_template('test_1.html', title='Home', user=user, form=form)