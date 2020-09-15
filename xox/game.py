from flask import session, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def game():
    session['answer'] = random.randint(1, 10)
    session['try_number'] = 1
    return redirect(url_for('play'))
    return 'Hello from Flask!'

