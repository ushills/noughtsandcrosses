from flask import Flask

app = Flask(__name__)

@app.route('/')
def game():
    return 'Hello from Flask!'

