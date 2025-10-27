from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Yee'}
    houses = [
        {'location': 'Ang Mo Kio', 'price': 500000 , "floor_area" : 100},
        {'location': 'Bishan', 'price': 600000, "floor_area" : 120},
        {'location': 'Clementi', 'price': 550000, "floor_area" : 140}
    ]

    return render_template('index.html', title='Home', user=user, houses=houses)