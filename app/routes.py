from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Murilo'}
    posts = [
        {
            'author': {'username': 'Murilo'},
            'body': 'Beautiful day in Petropolis'
        },
        {
            'author': {'username': 'David'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
