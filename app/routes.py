from app import app
from flask import render_template, redirect

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/portfolio')
def portfolio():
	return redirect('http://people.tamu.edu/~pdwarkanath/blog/posts/portfolio/', code=302)