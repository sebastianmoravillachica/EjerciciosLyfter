CREATE TABLE `product`(
    `id_product` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `code` BIGINT NOT NULL,
    `name` LINESTRING NOT NULL,
    `price` FLOAT(53) NOT NULL,
    `entry_date` DATE NOT NULL,
    `brand` LINESTRING NOT NULL,
    `stock_available` BIGINT NOT NULL
);
CREATE TABLE `invoices`(
    `id_invoice` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_number` BIGINT NOT NULL,
    `purchase_date` DATE NOT NULL,
    `buyer_email` LINESTRING NOT NULL,
    `total_amount` BIGINT NOT NULL
);
CREATE TABLE `products_per_invoice`(
    `id_products_invoice` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `quantity` INT NOT NULL,
    `total_amount` INT NOT NULL,
    `id_product` BIGINT NOT NULL,
    `id_invoice` BIGINT NOT NULL
);
CREATE TABLE `shopping_cart`(
    `id_shopping_cart` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `buyer_email` LINESTRING NOT NULL
);
CREATE TABLE `shopping_cart_items`(
    `id_product` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `id_shopping_cart` BIGINT NOT NULL,
    `quantity` INT NOT NULL,
    `id_shopping_cart_items` BIGINT NOT NULL,
    PRIMARY KEY(`id_shopping_cart_items`)
);
CREATE TABLE `user`(
    `id_user` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `full_name` MULTILINESTRING NOT NULL,
    `email` LINESTRING NOT NULL,
    `registration_date` DATE NOT NULL
);
ALTER TABLE
    `user` ADD UNIQUE `user_email_unique`(`email`);
CREATE TABLE `invoices_history`(
    `id_invoice` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_user` BIGINT NOT NULL
);
CREATE TABLE `reviews`(
    `id_review` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `product_code` BIGINT NOT NULL,
    `comment` MULTILINESTRING NOT NULL,
    `rating` SMALLINT NOT NULL,
    `date` DATE NOT NULL,
    `id_product` BIGINT NOT NULL,
    `id_user` BIGINT NOT NULL
);
CREATE TABLE `payment_methods`(
    `id_method` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `method_type` LINESTRING NOT NULL,
    `bank_name` LINESTRING NOT NULL,
    `id_invoice` BIGINT NOT NULL
);
ALTER TABLE
    `shopping_cart_items` ADD CONSTRAINT `shopping_cart_items_id_shopping_cart_foreign` FOREIGN KEY(`id_shopping_cart`) REFERENCES `shopping_cart`(`id_shopping_cart`);
ALTER TABLE
    `invoices` ADD CONSTRAINT `invoices_id_invoice_foreign` FOREIGN KEY(`id_invoice`) REFERENCES `invoices_history`(`id_invoice`);
ALTER TABLE
    `invoices_history` ADD CONSTRAINT `invoices_history_id_user_foreign` FOREIGN KEY(`id_user`) REFERENCES `user`(`id_user`);
ALTER TABLE
    `product` ADD CONSTRAINT `product_id_product_foreign` FOREIGN KEY(`id_product`) REFERENCES `products_per_invoice`(`id_product`);
ALTER TABLE
    `reviews` ADD CONSTRAINT `reviews_id_product_foreign` FOREIGN KEY(`id_product`) REFERENCES `product`(`id_product`);
ALTER TABLE
    `product` ADD CONSTRAINT `product_id_product_foreign` FOREIGN KEY(`id_product`) REFERENCES `shopping_cart_items`(`id_product`);
ALTER TABLE
    `products_per_invoice` ADD CONSTRAINT `products_per_invoice_id_invoice_foreign` FOREIGN KEY(`id_invoice`) REFERENCES `invoices`(`id_invoice`);
ALTER TABLE
    `payment_methods` ADD CONSTRAINT `payment_methods_id_invoice_foreign` FOREIGN KEY(`id_invoice`) REFERENCES `invoices`(`id_invoice`);
ALTER TABLE
    `reviews` ADD CONSTRAINT `reviews_id_user_foreign` FOREIGN KEY(`id_user`) REFERENCES `user`(`id_user`);