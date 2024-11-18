from flask import render_template
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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template(
        'login.html', 
        title = 'Вход', 
        form = form
        )