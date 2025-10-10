from flask import Flask,render_template,url_for,request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv("API_KEY")


@app.route("/",methods=["GET","POST"])
def index():
    result = None
    coin = None
    if request.method == "POST":
        coin = request.form['coin'].lower()
        API_URL = f"https://rest.coincap.io/v3/assets/{coin}?apiKey={API_KEY}"
        response = requests.get(API_URL)
        
        if response:
            data = response.json()
            cost = float(data['data']['priceUsd'])
            try:
               amount = float(request.form['number'])
               result = float(amount*cost)
              
            except ValueError:
                result = "Enter valid amount"
        else:
            result = "Enter valid Coin"
            
        
    else:
        pass   
    return render_template('index.html',result=result)

if __name__ == "__main__":
    app.run(debug=True)
