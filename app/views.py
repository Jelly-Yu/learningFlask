from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'Iris'}
	posts = [
		{
			'author': {'nickname': 'Jelly'},
			'body': 'It is cold outside'

		},
		{
			'author':{'nickname':'Jane'},
			'body': 'The snow was so heavy!'
		}
	]
	return render_template('index.html',
							title='Home',
							user=user,
							posts=posts)