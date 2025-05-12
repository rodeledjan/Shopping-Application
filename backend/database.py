import base64
import io
import sqlite3

from database import *   
from init_db import * 

database='database.db'

#do a idempotent create with describe/pragam....
def initialize_db():

    initialize_db()

    return 'Database has been initialized.'

def insert_product( product_name, description, category, price, image):

    con_insert = sqlite3.connect(database)
    cur_insert = con_insert.cursor()
    cur_insert.execute("INSERT INTO product_info(product_name,description,category,price,image) VALUES(?,?,?,?,?)",(product_name,description,category,price,image))
    con_insert.commit()
    cur_insert.close()
    con_insert.close()    

def view_inventory():

    # con2 = sqlite3.connect(database)
    con2 = sqlite3.connect(database)
    cur2 = con2.cursor()
    cur2.execute("SELECT * FROM product_info")
    con2.commit()
    result = cur2.fetchall()
    resultString = ''
    cur2.close()
    con2.close()    

    for row in result:
        for field in row:
            if isinstance(field, bytes):
                base64_bytes= base64.b64encode(field)
                base64_string= base64_bytes.decode('utf-8')
                field = '<img src="data:image/png;base64,'+ str(base64_string) +'" alt="Red dot" width="50" height="50"/>'

            resultString += f"""{field}"""
        resultString += '</br>'        
            
    resultString = '<div>'+ resultString +'</div>'
    return resultString 

def view_inventory_schema():
    
    con2 = sqlite3.connect(database)
    cur2 = con2.cursor()

    cur2.execute("SELECT * FROM sqlite_master")
    con2.commit()
    result = cur2.fetchall()
    resultString = ''

    cur2.close()
    con2.close()    

    return str(result)

def does_table_exists(table):
    
    table_exists_con = sqlite3.connect(database)
    table_existscur = table_exists_con.cursor()

    table_existscur.execute(f"SELECT * FROM sqlite_master WHERE NAME = '{table}'")
    table_exists_con.commit()
    result = table_existscur.fetchone()

    table_existscur.close()
    table_exists_con.close()    

    return result != None

def get_table_schema(table):
    
    table_exists_con = sqlite3.connect(database)
    table_existscur = table_exists_con.cursor()

    table_existscur.execute(f"SELECT * FROM sqlite_master WHERE NAME = '{table}'")
    table_exists_con.commit()
    result = table_existscur.fetchone()

    table_existscur.close()
    table_exists_con.close()    

    return str(result)
