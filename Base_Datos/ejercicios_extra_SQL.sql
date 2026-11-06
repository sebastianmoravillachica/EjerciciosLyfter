

-- Crear categorías y ajustar productos --

CREATE TABLE categories (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name varchar(100) UNIQUE NOT NULL,
description TEXT NOT NULL
);


ALTER TABLE products
	ADD category_id INTEGER REFERENCES categories(id);


INSERT INTO categories
    (name, description)
VALUES
    ('Tecnologia', 'Productos electrónicos, dispositivos y accesorios tecnológicos.'),
    ('Alimentos', 'Productos alimenticios y bebidas para consumo.'),
    ('Ropa', 'Prendas de vestir y accesorios de moda para diferentes ocasiones.');

UPDATE products SET

category_id=1

where id IN (1,2);


SELECT * FROM products;

-- Carga de productos y filtros básicos --
INSERT INTO products
    (code, name, price, entry_date, brand, stock_available, category_id)
VALUES
    -- Tecnología (category_id = 1)
    (1003, 'Teclado', 25000.00, '2026-10-10', 'Logitech', 20, 1),
    (1004, 'Monitor', 95000.00, '2026-10-11', 'Samsung', 10, 1),
    (1005, 'Audifonos', 18000.00, '2026-10-12', 'Sony', 25, 1),

    -- Alimentos (category_id = 2)
    (1006, 'Arroz', 1500.00, '2026-10-13', 'Tio Pelon', 50, 2),
    (1007, 'Leche', 1200.00, '2026-10-14', 'Dos Pinos', 30, 2),
    (1008, 'Cafe', 3500.00, '2026-10-15', '1820', 40, 2),

    -- Ropa (category_id = 3)
    (1009, 'Camisa', 12000.00, '2026-10-16', 'Nike', 15, 3),
    (1010, 'Pantalon', 20000.00, '2026-10-17', 'Levis', 12, 3);

SELECT * FROM products;

SELECT * FROM products WHERE price>50000;

SELECT * FROM products WHERE name LIKE "%apple%";

SELECT * FROM products ORDER BY price DESC LIMIT 5;

-- Correcciones de datos en productos --

UPDATE products SET

stock_available=0

where price <= 0;


UPDATE products SET

price=price+100

where stock_available < 10;

UPDATE products SET

stock_available=stock_available-1

where id = 10;


SELECT * FROM products ORDER BY id ASC LIMIT 10;