from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Admin'}
    posts = [
        {
            'id': 1,
            'author': {'username': 'Zee'},
            'body': 'Шутки про говно не смешные (скорее всего)'
        },
        {
            'id': 2,
            'author': {'username': 'Саня'},
            'body': 'Ты нахуя меня сюда добавил?)'
        }
    ]
    comments = [
        {
            'id': 1,
            'post_id': 1,
            'author': {'username': 'Саня'},
            'body': 'Ты заебал. Убери меня отсюда.'
        }
    ]
    return render_template(
        'index.html', 
        title = 'Домашняя страница', 
        user = user, 
        posts = posts,
        comments = comments
        )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template(
        'login.html', 
        title='Sign In', 
        form=form)