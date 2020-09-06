
from flask import Flask, render_template
import requests
app = Flask(__name__)

# Define homepage view
@app.route('/')
def getData():
    
    # Get data from API
    response = requests.get("https://api.usaspending.gov/api/v2/references/toptier_agencies/")
    # Convert data to json
    data = response.json()

    return render_template("table.html", data=data['results'])

# We only need this for local development.
if __name__ == '__main__':
    app.run()
