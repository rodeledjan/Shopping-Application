--DROP TABLE product_info
--DROP TABLE users
CREATE TABLE IF NOT EXISTS product_info (
   id INTEGER PRIMARY KEY AUTOINCREMENT
    , product_name TEXT NOT NULL
    , description TEXT NOT NULL 
    , category TEXT NOT NULL
    , price REAL
    , image BLOB NOT NULL 
);

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    , email TEXT UNIQUE
    , firstname TEXT NOT NULL 
    , lastname TEXT NOT NULL               
    , password TEXT
);