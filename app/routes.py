from flask import render_template
from app import app

@app.route('/')
@app.route('/imdex')
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