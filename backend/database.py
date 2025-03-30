import sqlite3
#create a database
# con = sqlite3.connect("Inventory.db", check_same_thread=False)

# con = sqlite3.connect("Inventory.db")

# #create tables
# cur = con.cursor()

# #delete table records to start from beginning.  For demo purposes only. 
# # sql = "DROP TABLE movie"
# # cur.execute(sql)

# #cur.execute("CREATE TABLE product(Product name, Description, Category, Price, Image, Seller_id)")
# #cur.execute("CREATE TABLE product_info(Productname, Description, Category, Price, Image, Seller_id)")
# cur.execute("CREATE TABLE product_info2(Productname, Description, Category, Price, Image, Seller_id)")
# con.commit()

# cur.close()
# con.commit()
##display product info columns
#cur.execute(f"PRAGMA table_info({'product_info'});")
# columns = cur.fetchall()

##display each column in a new line
# for column in columns:
#     print(column)

# cur.execute(f"INSERT INTO product_info VALUES('product_2', 'Description_2','Category_2','20','image2','seller_id2')")

# #print(f"INSERT INTO product_info VALUES('product_1', 'Description_1','Category_1','10','image','seller_id')")

# con.commit()

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

def insert_product( product_name, description, category, price, image, seller_id):

    con_insert = sqlite3.connect("Inventory.db", check_same_thread=False)
    cur_insert = con_insert.cursor()
    
    cur_insert.execute(f"INSERT INTO product_info2 VALUES('{product_name}','{description}','{category}','{price}','{image}','{seller_id}')")
    con_insert.commit()

    cur_insert.close()
    con_insert.close()    

def view_inventory():

    # con = sqlite3.connect("Inventory.db", check_same_thread=False)
    # cur = con.cursor()
    # cur.execute("CREATE TABLE product_info2(Productname, Description, Category, Price, Image, Seller_id)")
    # con.commit()
    
    # sql = "DROP TABLE product_info2"
    # cur.execute(sql)

    con2 = sqlite3.connect("Inventory.db", check_same_thread=False)
    cur2 = con2.cursor()

    cur2.execute("SELECT * FROM product_info2")
    con2.commit()
    result = cur2.fetchall()

    resultString = ''

    # for item in result:
    #     resultString += f"""Movie:{item[0]}<br>
    #     Year: {item[1]}
        # <br>Score:{item[2]}<br><br>"""
    for item in result:
        resultString += f"""{item}<br>"""

    cur2.close()
    con2.close()    

    return resultString #str(result) 

