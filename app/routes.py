from app import app
from flask import render_template
import pyfirmata
import time


board = pyfirmata.Arduino('COM3')

it = pyfirmata.util.Iterator(board)
it.start()



# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'username': 'Miguel'}
#     posts = [
#         {
#             'author': {'username': 'John'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'username': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/')
@app.route('/on/')
def on():
    board.digital[13].write(1)
    return render_template('onOff.html')

@app.route('/off/')
def off():
    board.digital[13].write(0)
    return render_template('onOff.html')