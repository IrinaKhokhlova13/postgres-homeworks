-- SQL-команды для создания таблиц

-- Создала через командную строку базу данных north
CREATE DATABASE north



-- Создать три таблицы, используя query tool в pgAdmin:  employees, customers и orders
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name text,
	last_name text,
	title text NOT NULL,
	birth_date date,
	notes text
);


CREATE TABLE customers
(
	customer_id varchar(10) PRIMARY KEY,
	company_name text,
	contact_name text
);


CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(10) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date,
	ship_city text
);


-- Зайти в pgAdmin и убедиться, что данные в таблицах есть
SELECT * FROM customers
SELECT * FROM employees
SELECT * FROM orders