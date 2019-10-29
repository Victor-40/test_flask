from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import FindForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Victor"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/find_builds', methods=['GET', 'POST'])
def find_builds():
    form = FindForm()
    if form.validate_on_submit():
        flash("Find build {}, tag {}".format(form.build.data, form.tag.data))
        return redirect(url_for('result'))
    return render_template('find_builds.html', title='Find', form=form)


@app.route('/result')
def result():
    setups = ["111111111111", "22222222222222", "3333333333333", "44444444444444"]
    setups_count = len(setups)

    return render_template('result.html', title='Result', setups=setups, setups_count=setups_count)
