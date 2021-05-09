from Flask import request

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your Browser is {}'.format(user_agent)