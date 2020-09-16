import os
from flask import Flask, session, redirect, url_for, request, render_template
import xox.services.xox as xox

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    'Not_very_secret'

@app.route('/')
def game():

    # session['try_number'] = 1
    # return redirect(url_for('play'))
    return "Draw board here"

@app.route('/new-game')
def new_game():
    game = xox.XOXGame()
    session['board'] = game.board
    return "Init game"