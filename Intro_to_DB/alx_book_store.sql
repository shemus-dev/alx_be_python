CREATE DATABASE ALX_BOOK_STORE;
USE ALX_BOOK_STORE;

CREATE TABLE AUTHORS (
    author_id int auto_increment PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

CREATE  TABLE BOOKS   (
    book_id INT auto_increment PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    Foreign Key (author_id) REFERENCES AUTHORS(author_id)

);

CREATE TABLE CUSTOMERS  (
    customer_id INT auto_increment PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215),
    address TEXT
);

CREATE Table ORDERS  (
    order_id INT auto_increment PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    Foreign Key (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE ORDER_DETAILS(
    orderdetailid INT auto_increment PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE,
    FOREIGN KEY (order_id) REFERENCES ORDERS(order_id),
    FOREIGN KEY (book_id) REFERENCES BOOKS(book_id)
);