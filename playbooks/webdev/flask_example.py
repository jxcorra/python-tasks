import datetime

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')  # добавление view используя декоратор
def hello_world():
    return 'Hello World!'


def question_of_life():
    return


# redirect
@app.route('/welcome/<string:username>')
def welcome_user(username: str):
    return redirect(url_for('dashboard', user=username))


@app.route('/dashboard/<user>')
def dashboard(user):
    return f'Dashboard of {user}'


# form views
@app.route('/success/<name>')
def success(name):
    return render_template('welcome.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.add_url_rule('/qol', 'qol', question_of_life)  # добавление view без декоратора
    app.run()  # host, port, debug, options are optional
