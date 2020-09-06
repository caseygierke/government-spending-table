# app.py

from flask import Flask, render_template
app = Flask(__name__)

# Define homepage view
@app.route('/')
def getData():
    
    return render_template("table.html")

# We only need this for local development.
if __name__ == '__main__':
    app.run()
