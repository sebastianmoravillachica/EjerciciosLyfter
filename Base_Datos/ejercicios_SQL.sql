-- SQLite


--- CREACION DE TABLAS ---
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code bigint NOT NULL,
    name VARCHAR(25) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    entry_date DATE NOT NULL,
    brand VARCHAR(25) NOT NULL,
    stock_available INT NOT NULL
);


CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(254) NOT NULL UNIQUE,
    registration_date DATE NOT NULL
);


CREATE TABLE invoices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number INT NOT NULL UNIQUE,
    purchase_date DATE NOT NULL,
    total_amount DECIMAL(10,2) DEFAULT 0,
    user_id INTEGER REFERENCES users(id)
);


CREATE TABLE products_per_invoice(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quantity INT NOT NULL DEFAULT 0,
    total_amount INT DEFAULT 0,
    product_id INTEGER REFERENCES products(id),
    invoice_id INTEGER REFERENCES invoices(id)
);

CREATE TABLE shopping_cart(
id INTEGER PRIMARY KEY AUTOINCREMENT,
buyer_email VARCHAR(254) NOT NULL UNIQUE
);


CREATE TABLE shopping_cart_items(
id INTEGER PRIMARY KEY AUTOINCREMENT,
quantity INT DEFAULT 0,
product_id INTEGER REFERENCES products(id),
shopping_cart_id INTEGER REFERENCES shopping_cart(id)
);

CREATE TABLE payment_methods(

id INTEGER PRIMARY KEY AUTOINCREMENT,
method_type VARCHAR(50) NOT NULL,
bank_name VARCHAR(100)
);

CREATE TABLE payment_method_per_invoice(
id INTEGER PRIMARY KEY AUTOINCREMENT,
invoice_id INTEGER REFERENCES invoices(id),
method_id INTEGER REFERENCES payment_methods(id)
);

--- MODIFICACIONES ----
ALTER TABLE invoices
	ADD phone_number VARCHAR(20);

ALTER TABLE invoices
	ADD employee_id VARCHAR(20);

---- AGREGAR DATOS ---
INSERT INTO products
    (code, name, price, entry_date, brand, stock_available)
VALUES
    (1001, 'Laptop', 75000.00, '2026-10-01', 'Lenovo', 15),
    (1002, 'Mouse', 15000.00, '2026-10-05', 'Logitech', 40);


INSERT INTO user
    (full_name, email, registration_date)
VALUES
    ('Carlos Ramirez', 'carlos@example.com', '2026-09-01'),
    ('Maria Fernandez', 'maria@example.com', '2026-09-10');

INSERT INTO invoices
    (invoice_number, purchase_date, total_amount,
    user_id, phone_number, employee_id)
VALUES
    (1234567891, '2026-10-15', 150000,
    2, '+50688881234', 'EMP-00001'),

    (1234567890, '2026-10-20', 375000,
    2, '+50687771234', 'EMP-00002');

INSERT INTO products_per_invoice
    (quantity, total_amount, product_id, invoice_id)
VALUES
    (2, 150000, 1, 2),
    (5, 375000, 1, 3);


INSERT INTO shopping_cart (buyer_email)
VALUES
    ('carlos@example.com'),
    ('maria@example.com');

INSERT INTO shopping_cart_items
    (quantity, product_id, shopping_cart_id)
VALUES
    (2, 1, 1),
    (3, 2, 2);


INSERT INTO payment_methods
    (method_type, bank_name)
VALUES
    ('Credit Card', 'BAC Credomatic'),
    ('Bank Transfer', 'Banco Nacional');

INSERT INTO payment_method_per_invoice
    (invoice_id, method_id)
VALUES
    (2, 1),
    (3, 2);

--- CONSULTAS ---

SELECT * FROM products;

SELECT * FROM products where price > 50000;

SELECT * FROM products_per_invoice where invoice_id = 3;

SELECT product_id, SUM(quantity) AS total_purchased FROM products_per_invoice
GROUP BY product_id;

SELECT * from invoices where user_id = 2;

SELECT * FROM invoices ORDER BY total_amount DESC;

SELECT * FROM invoices where invoice_number =1234567890;


--- COMANDOS QUE UTILIZA PARA SOLUCIONAR LOS ERRORES

ALTER TABLE user RENAME TO users

DROP TABLE invoices;


CREATE TABLE invoices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number INT NOT NULL UNIQUE,
    purchase_date DATE NOT NULL,
    total_amount DECIMAL(10,2) DEFAULT 0,
    user_id INTEGER REFERENCES users(id)
);


SELECT * FROM products_per_invoice where invoice_id = 3;