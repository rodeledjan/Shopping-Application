import sqlite3

# cur.execute(f"SELECT * FROM product_info")
# con.commit()

# product_info =cur.fetchall()
# print(str(product_info))    

# resultString = ''

# for item in result:
#     resultString += f"""Movie:{item[0]}<br>
#     Year: {item[1]}
#     <br>Score:{item[2]}<br><br>"""

#do a idempotent create with describe/pragam....

def initialize_db():
    con = sqlite3.connect("Inventory.db", check_same_thread=False)
    cur = con.cursor()
    
    # cur.execute("DROP TABLE product_info")
    # con.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS product_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    , product_name TEXT NOT NULL
    , description TEXT NOT NULL 
    , category TEXT NOT NULL
    , price REAL
    , image BLOB NOT NULL 
    , seller_id INTEGER)''')
    
    con.commit()


    data = [
        {
            "table":"product_info"
            , "columns":"product_name, description, category, price, image, seller_id"
        },
        # {
        #     "table":"Test_Table"
        #     , "columns":"product_name, description, category, price, image, seller_id"
        # },
        ]
    
    
    # add_columns=''

    # for item in data:
    #     #creates an idempotent table
    #     result = does_table_exists(str(item["table"]))
    #     if result != True:
    #         cur.execute(
    #             f"CREATE TABLE {item["table"]}" +
    #              '(' + (item["columns"]) + ')' )

    #     create_table = ''
    #     create_table = f"CREATE TABLE {item["table"]}" 
    #     add_columns = '(' + (item["columns"]) + ')'
    #     create_table = create_table + add_columns

    con.commit()
    cur.close()
    con.close()    

    return 'Database has been initialized.'

def insert_product( product_name, description, category, price, image, seller_id):

    con_insert = sqlite3.connect("Inventory.db", check_same_thread=False)
    cur_insert = con_insert.cursor()
    
    cur_insert.execute(f"INSERT INTO product_info VALUES('{product_name}','{description}','{category}','{price}','{image}','{seller_id}')")
    con_insert.commit()

    cur_insert.close()
    con_insert.close()    

def view_inventory():

    con2 = sqlite3.connect("Inventory.db", check_same_thread=False)
    cur2 = con2.cursor()

    cur2.execute("SELECT * FROM product_info")
    con2.commit()
    result = cur2.fetchall()
    resultString = ''

    for item in result:
        for i in item:

            # resultString += f"""{item}<br>"""
            resultString += f"""{i}<br>"""
            
        # resultString = str(item)

    cur2.close()
    con2.close()    

    return str(resultString) 

def view_inventory_schema():
    
    con2 = sqlite3.connect("Inventory.db")
    cur2 = con2.cursor()

    cur2.execute("SELECT * FROM sqlite_master")
    con2.commit()
    result = cur2.fetchall()
    resultString = ''

    cur2.close()
    con2.close()    

    return str(result)

def does_table_exists(table):
    
    table_exists_con = sqlite3.connect("Inventory.db")
    table_existscur = table_exists_con.cursor()

    table_existscur.execute(f"SELECT * FROM sqlite_master WHERE NAME = '{table}'")
    table_exists_con.commit()
    result = table_existscur.fetchone()

    table_existscur.close()
    table_exists_con.close()    

    return result != None

def get_table_schema(table):
    
    table_exists_con = sqlite3.connect("Inventory.db")
    table_existscur = table_exists_con.cursor()

    table_existscur.execute(f"SELECT * FROM sqlite_master WHERE NAME = '{table}'")
    table_exists_con.commit()
    result = table_existscur.fetchone()

    table_existscur.close()
    table_exists_con.close()    

    return str(result)
