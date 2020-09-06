
from flask import Flask, render_template, request
import requests
app = Flask(__name__)

# Define homepage view
@app.route('/', methods=['GET', 'POST'])
def getData():
    
    if request.method == 'POST':
        
        # Get data from API
        response = requests.get("https://api.usaspending.gov/api/v2/references/toptier_agencies/")
        # Convert data to json
        data = response.json()
    
        return render_template("table.html", data=data['results'])
        
    else:
    
        return render_template("table.html")

# We only need this for local development.
if __name__ == '__main__':
    app.run()
