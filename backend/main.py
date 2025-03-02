from flask import Flask, request, jsonify
import requests
import sqlite3
import os
from dotenv import load_dotenv 

load_dotenv()

app = Flask(__name__)

@app.route('/') #home url/just like Index.html
def homeroute():
    return 'Hello World'

@app.route('/currency_converter') #home url/just like Index.html
def currency_converter():
    # source_curr = request.args.get('source_curr')
    # target_curr = request.args.get('target_curr')
    # amount = float(request.args.get('amount'))
    
    #make sure that variables are not empty

    source_curr = 'USD'
    target_curr = 'INR'
    amount = 10
    
    variable_data = jsonify(source_curr, target_curr, amount)

    print (variable_data)

    api_key = os.getenv('CURRENCY_CONVERTER_KEY') 
   
    #make the api return an error response
    # api_key = api_key + 'fwse'

    api_url = 'https://v6.exchangerate-api.com/v6/{}/latest/'.format(api_key)

    response = requests.get(f"{api_url}{source_curr}")

    #check for status
    if response.status_code != 200:
        return response.text
    
    else:
        data = response.json()
        rates = data['conversion_rates']
        converted_amount = amount * rates[target_curr]
        
        return str(converted_amount)

if __name__ == '__main__':
    app.run(debug=True)
