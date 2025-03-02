import sqlite3
#create a database
con = sqlite3.connect("Inventory.db")

#create tables
cur = con.cursor()

#delete table records to start from beginning.  For demo purposes only. 
# sql = "DROP TABLE movie"
# cur.execute(sql)

cur.execute("CREATE TABLE product(Product name, Description, Category, Price, Image, Seller_id)")

cur.execute(f"PRAGMA table_info({'product'});")

columns = cur.fetchall()

print(columns)

#do a idempotent create with describe/pragam....
