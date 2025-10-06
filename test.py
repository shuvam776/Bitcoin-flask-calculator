from flask import Flask,render_template,url_for,request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"
response = requests.get(API_URL)
data = response.json()
print(data)