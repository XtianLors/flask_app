from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return '<h1>Hello there!</h1>'+'<p>Your Browser is {}'.format(user_agent)

@app.route('/user/<username>'):
def user(username):
	return '<h1>Hello, {}!'.format(username)