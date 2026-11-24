

-- Ejercicio Orders

-- 1FN:
-- Se identifican los datos de clientes, órdenes y productos.
-- Los productos de una orden deben almacenarse individualmente,
-- sin listas de productos dentro de una sola columna.

-- 2FN:
-- Se separan customers, items y order_items.
-- Los datos del cliente dependen de customer_id.
-- Los datos del producto dependen de item_id.
-- La cantidad y solicitud especial dependen de la orden
-- y del producto que contiene.

-- 3FN:
-- Se evita almacenar el nombre y teléfono del cliente
-- directamente en orders.
-- Estos datos dependen de customer_id, no de order_id.
-- La dirección se conserva en orders porque corresponde
-- a la entrega específica de cada orden.


CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);


CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(150) NOT NULL,
    price DECIMAL(8, 2) NOT NULL
);


CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    address VARCHAR(255) NOT NULL,
    delivery_time DATETIME NOT NULL,
    customer_id INTEGER NOT NULL,

    FOREIGN KEY (customer_id)
        REFERENCES customers(id)
);


CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    quantity INT NOT NULL,
    special_request TEXT,
    unit_price DECIMAL(10, 2) NOT NULL,
    order_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,

    FOREIGN KEY (order_id)
        REFERENCES orders(id),

    FOREIGN KEY (item_id)
        REFERENCES items(id)
);





-- Ejercicio Cars
-- Normalización hasta la Tercera Forma Normal (3FN)


-- 1FN:
-- Los datos se almacenan en valores individuales.
-- No se guardan varios propietarios en una misma columna.
-- Cada vehículo tiene un VIN único.

-- 2FN:
-- Se separan los vehículos y propietarios.
-- Los datos del vehículo dependen del VIN.
-- Los datos del propietario dependen de owner_id.
-- La relación entre vehículo y propietario se almacena
-- en car_owners, ya que depende de ambos identificadores.

-- 3FN:
-- Se crea vehicle_models porque brand, model y year
-- describen el modelo y no el vehículo individual.
--
-- Se crean insurance_companies e insurance_policies
-- para evitar repetir el nombre de la compañía en cada póliza.
--
-- Se crea car_insurances para registrar la relación
-- entre vehículos y pólizas.


CREATE TABLE owners (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);


CREATE TABLE colors (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL UNIQUE
);


-- Información compartida por vehículos del mismo modelo
CREATE TABLE vehicle_models (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL
);


-- Vehículos individuales
CREATE TABLE cars (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    VIN_number VARCHAR(17) NOT NULL UNIQUE,
    model_id INTEGER NOT NULL,
    color_id INTEGER NOT NULL,

    FOREIGN KEY (model_id)
        REFERENCES vehicle_models(id),

    FOREIGN KEY (color_id)
        REFERENCES colors(id)
);


-- Relación entre vehículos y propietarios
CREATE TABLE car_owners (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    car_id INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    ownership_start DATE,
    ownership_end DATE,

    FOREIGN KEY (car_id)
        REFERENCES cars(id),

    FOREIGN KEY (owner_id)
        REFERENCES owners(id),

    UNIQUE (car_id, owner_id, ownership_start)
);


-- Compañías aseguradoras
CREATE TABLE insurance_companies (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE
);


-- Pólizas ofrecidas por cada compañía
CREATE TABLE insurance_policies (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    insurance_policy VARCHAR(50) NOT NULL,
    company_id INTEGER NOT NULL,

    FOREIGN KEY (company_id)
        REFERENCES insurance_companies(id),

    UNIQUE (company_id, insurance_policy)
);


-- Relación entre vehículos y pólizas
CREATE TABLE car_insurances (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    car_id INTEGER NOT NULL,
    policy_id INTEGER NOT NULL,
    start_date DATE,
    end_date DATE,

    FOREIGN KEY (car_id)
        REFERENCES cars(id),

    FOREIGN KEY (policy_id)
        REFERENCES insurance_policies(id)
);
