from flask import Flask, request, render_template	
from markupsafe import escape


app = Flask(__name__) #Instance of Flask class -> File localizer: WSGI application
'''convenient shortcut for creating an instance of Flask. Searches for templates and satic files.'''
#Keeps mapping of URL's to python functions.
#Declaring the decorator @app.route
#@app.route('/') tells Flask what URL should trigger our function.
@app.route('/')#route is the association between a URL and the function that handles. It is defined in the URL map
def index():
	user_agent = request.headers.get('User-Agent')
	render_template('index.html')
	return f'<p>Your browser is {escape(user_agent)}</p>'

#If another program is already using port 5000, you’ll see OSError: [Errno 98] or OSError: [WinError 10013] when the server tries to start.

#Adding protection with escape()
@app.route('/user/<username>')
def user(username):
	Flask.render_template('user.html', name=name)
	return '<h1>Hello, {}!</h1>'.format(escape(username))#using escape to avoid injection attacks
#The (HEAD, OPTIONS, GET) elements shown in the URL map are the request methods that are handled by the routes.
#The HTTP specification
#The three routes to the url map are attached to the GET method, which is used when the client whants to request for  information.

#view: A view function is the code you write to respond to requests to your application.
#Decorator: Because each view in Flask is a function, decorators can be used to inject additional functionality to one or more functions.
#Blueprint: A Blueprint is a way to organize a group of related views and other code.Flaskr will have two blueprints, one for authentication functions and one for the blog posts functions.
#Route: Decorate a view function to register it with the given URL rule and options. Calls add_url_rule(), which has more details about the implementation.
#handler: is a routine/function/method which is specialized in a certain type of data or focused on certain special tasks.
	#Event Handler: receives and digests events and signals from the surrounding system (e.g. OS or GUI)
	#Memory handler: performs certain special tasks on memory.
	#File input handler -  function receiving file input and performing special tasks on the data, all depending on context of course.
#Contexts: these are meant to provide certain data that the view function needs in order to fulfill the request
		#contexts enable flask to make certain variables globally accesible to a thread without interferring in the other threads.
		#Application context: current_app -> The application instance for the active. g -> An object that the application can use for a temporary storage during the handling of a request.
		#Request context: request -> The request object, which encapsulates the contents of an HTTP request sent by the client. session -> The user session, a dictionary the the application can use to store values that are "remembered" between requests.
	#Static files: 

	##https://flask.palletsprojects.com/en/2.1.x/quickstart/#a-minimal-application

	#Flask pushes the application and request context before dispatching a request to the application, and removes them after
	# the request is handled. When the application is pushed the current_app and g value become available to the thread.

"""For older version of flask the
if __name__ == '__main__':
	app.run()
In recent versions of flask this instance is substituted by  flask run command in the command line.
"""

