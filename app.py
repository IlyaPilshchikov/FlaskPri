from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return 'Ура, моё первое приложение!!!!!!!'


@app.route('/help/')
def help():
    return '<h1>Ждите и помощь будет оказана</h1>'


@app.route('/<user>/')
def login(user):
    return f'<h1> Здравствуйте, наш дорогой и любимый {user} </h1>'


@app.route('/<int:id>/')
def num(id):
    return f'<h1> Ваш номер - {id} </h1>'


if __name__ == '__main__':
    app.run(debug=True)
