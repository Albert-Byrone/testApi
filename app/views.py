from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its content
    '''
    title = 'Home welcome to the Best Movies review online'
    return render_template('index.html',title = title)
    
@app.route('/movie/<movie_id>')
def movies(movie_id):
    '''
    View movie page thet returns the movie details page and details
    '''
    return render_template('movie.html',id = movie_id)