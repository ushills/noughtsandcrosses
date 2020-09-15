import os
from flask import Flask, session, redirect, url_for, request, render_template
import xox.services.xox as xox

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    'Not_very_secret'

@app.route('/')
def game():
    game = xox.XOXGame()
    session['board'] = game.board
    # session['try_number'] = 1
    # return redirect(url_for('play'))
    return str(session['board'])

