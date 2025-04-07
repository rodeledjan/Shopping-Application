from flask import Flask, request, jsonify
import requests
import sqlite3
import os
from dotenv import load_dotenv 

# from database import insert_product 
# from database import view_inventory
# from database import view_inventory_schema
from database import *
load_dotenv()

app = Flask(__name__)

@app.route('/') #home url/just like Index.html
def homeroute():
    # initialize_db()
    #return 'Hello World'
    return 'Hello World.  ' + initialize_db()

@app.route('/currency_converter') #home url/just like Index.html
def currency_converter():
    # source_curr = request.args.get('source_curr')
    # target_curr = request.args.get('target_curr')
    # amount = float(request.args.get('amount'))
    
    #make sure that variables are not empty

    source_curr = "USD"
    target_curr = "IN"
    amount = 0.0

    variables_dict: dict[str, str,float] = {
        "source_curr": source_curr,
        "target_curr": target_curr,
        "amount": amount
        }

    variables_dict_copy = {}

    for x in variables_dict:
        if type( variables_dict[x] ) == str:
            if len(variables_dict[x]) != 3:
                #remove if it the variable is good: string and has length of 3,
                variables_dict_copy[x] = variables_dict[x]

        elif type( variables_dict[x] ) == float:
            if variables_dict[x] < 1:
                #remove if it the variable is good: float and above 1
                variables_dict_copy[x] = variables_dict[x]

    error = "Error found with the following items: "
    if len(variables_dict_copy) >  0:
        
        json_variables = jsonify( variables_dict_copy )

        for x, y in variables_dict_copy.items():
            error = error + '<br>' + '-' + x + ': ' + str(y)            

        return error

    # variable_data = jsonify(source_curr, target_curr, amount)

    # print (variable_data)

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

@app.route('/add_inventory') #let's user add a product to the inventory
def add_inventory():

    # #Product name, Description, Category, Price, Image, Seller_id)")
    product_name = request.args.get('product_name')
    description = request.args.get('description')
    category = request.args.get('category')
    price = request.args.get('price')
    
    # image = 'image'
    
    with open(r'images/pantene.png', 'rb') as file:
        img_data = file.read()

    
    # #image = request.args.get('image')
    # # with open('/Users/rodeledjan/Documents/GitHub/Shopping-Application/images/Screenshot 2025-03-23 at 3.46.03 PM.png',"rb") as f:
    # #     image = f.read()    
    seller_id = request.args.get('seller_id')
    
    #/add_inventory?product_name=Crest&description=toothpaste&category=bath&price=4&seller_id=1
    #add_inventory?product_name=Safeguard&description=soap&category=bath&price=4&seller_id=1

    result = f"{product_name},{description},{category},{price},{img_data},{seller_id})"

    try:
        insert_product(product_name,description,category,price, img_data,seller_id)
                 
        return 'insert successful'
    
    except Exception as e:
        return str(e)


@app.route('/inventory') #view products in the database
def viewinventory():
   
   return view_inventory()


@app.route('/view_schema') 
def view_schema():

    return view_inventory_schema()

@app.route('/table/schema') #view products in the database
def table_schema():
    table = request.args.get("table")

    return get_table_schema(table)


@app.route('/table/create') #view products in the database
def table_create():
  
    return initialize_db();

if __name__ == '__main__':
    app.run(debug=True)