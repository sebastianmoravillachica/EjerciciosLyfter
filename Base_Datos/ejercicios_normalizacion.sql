--- Ejercicio Orders ---


--- Utilice 4 tablas para asi poder separar mejor las tablas y reducir errores, 
--- cree una tabla intermediaria entre orders y items para tener un registro por orden y agregue address en orders ya que un customer puede tener diferentes direcciones

CREATE TABLE customers(
    id INTEGER PRIMARY KEY  AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE items(
    id INTEGER PRIMARY KEY  AUTO_INCREMENT,
    item_name VARCHAR(150) NOT NULL,
    price DECIMAL(8, 2) NOT NULL
);

CREATE TABLE orders(
    id INTEGER PRIMARY KEY  AUTO_INCREMENT,
    address VARCHAR(255) NOT NULL,
    delivery_time DATETIME NOT NULL,
    customer_id INTEGER REFERENCES customers(id)
);

CREATE TABLE order_items(
    id INTEGER PRIMARY KEY  AUTO_INCREMENT,
    quantity INT NOT NULL,
    special_request TEXT,
    unit_price DECIMAL(10,2) NOT NULL,
    order_id INTEGER REFERENCES order(id),
    item_id INTEGER REFERENCES items(id)
);




--- Ejercicio Cars ---

--- En este ejercicio aproveche que cars puede ser una tabla intermediaria, 
--- cree el VIN number como unico ya que realmente el VIN solo puede pertenecer a un vehiculo, cree un tabla colores ya que eso puede que se repita mcuhas veces, 

CREATE TABLE owners(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(150) NOT NULL,
phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE colors(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(30) NOT NULL,
);

CREATE TABLE insurances(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(100) NOT NULL,
insurance_policy VARCHAR(50) NOT NULL
);

CREATE TABLE cars(
id INTEGER PRIMARY KEY AUTOINCREMENT,
brand VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
year INTEGER NOT NULL,
VIN_number VARCHAR(17) UNIQUE NOT NULL,
owner_id INTEGER REFERENCES owners(id),
color_id INTEGER REFERENCES colors(id),
insurance_id INTEGER REFERENCES insurances(id),
);