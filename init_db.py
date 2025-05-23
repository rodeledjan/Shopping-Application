import sqlite3

def initialize_db():

    connection = sqlite3.connect('database.db')

    with open('backend/schema.sql') as f:
        sql_script = f.read()

    connection.executescript(sql_script)
    cur = connection.cursor()
    
    # Need to create a loop out of this 
    # products = [
    # #     ('Crest', 'Toothpaste','Oral Care', 3.45 ),
    # #     ('Pantene', 'Shampoo','Hair Care', 2.25 ),
    # #     ('Safeguard', 'Bar Soap','Body Soap', 3.00 ),

    # # ]

    with open('/Users/rodeledjan/Documents/GitHub/Shopping-Application/images/crest_3D_white.png',"rb") as f:
        image = f.read()  

    cur.execute("INSERT INTO product_info(product_name,description,category,price,image) VALUES(?,?,?,?,?)",
                ('Crest', 'Toothpaste','Oral Care', 3.45 ,image))

    with open('/Users/rodeledjan/Documents/GitHub/Shopping-Application/images/pantene.png',"rb") as f:
        image = f.read()  
    cur.execute("INSERT INTO product_info(product_name,description,category,price,image) VALUES(?,?,?,?,?)",
                ('Pantene', 'Shampoo','Hair Care', 2.25,image))

    with open('/Users/rodeledjan/Documents/GitHub/Shopping-Application/images/safeguard.png',"rb") as f:
        image = f.read()  
    cur.execute("INSERT INTO product_info(product_name,description,category,price,image) VALUES(?,?,?,?,?)",
                ('Safeguard', 'Bar Soap','Body Soap', 3.00,image))

    # cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
    #             ('Second Post', 'Content for the second post')
    #             )

    connection.commit()
    connection.close()

    return "Database has been initialized."