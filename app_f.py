from flask import Flask
from flask import request

app = Flask(__name__) #Instance of Flask class -> File localizer: WSGI application
'''convenient shortcut for creating an instance of Flask. Searches for templates and satic files.'''
#Keeps mapping of URL's to python functions.
#Declaring the decorator @app.route
#@app.route('/') tells Flask what URL should trigger our function.
@app.route('/')#route is the association between a URL and the function that handles. 
def index():
	return '<h1>Bad Request</h1>', 400

@app.route('x')
def user(username):
	return '<h1>Hello, {}!</h1>'.format(username)

#view: A view function is the code you write to respond to requests to your application.
#Decorator: Because each view in Flask is a function, decorators can be used to inject additional functionality to one or more functions.
#Blueprint: A Blueprint is a way to organize a group of related views and other code.Flaskr will have two blueprints, one for authentication functions and one for the blog posts functions.
#Route: Decorate a view function to register it with the given URL rule and options. Calls add_url_rule(), which has more details about the implementation.
#handler: is a routine/function/method which is specialized in a certain type of data or focused on certain special tasks.
	#Event Handler: receives and digests events and signals from the surrounding system (e.g. OS or GUI)
	#Memory handler: performs certain special tasks on memory.
	#File input handler -  function receiving file input and performing special tasks on the data, all depending on context of course.

	##https://flask.palletsprojects.com/en/2.1.x/quickstart/#a-minimal-application


