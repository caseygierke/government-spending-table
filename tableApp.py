# app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def initial_app():
    return '<h1>Ummm, is this thing on?</h1>'

# We only need this for local development.
if __name__ == '__main__':
    app.run()
