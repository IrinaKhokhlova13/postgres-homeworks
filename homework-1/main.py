"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from pathlib import Path
from config import ROOT_DIR
import csv


#чтение из csv файла
def rm_file(name_file):
    file_path = Path(ROOT_DIR, f'north_data/{name_file}')
    with open(file_path, encoding='utf-8') as f:
        reader_dict = []
        reader = csv.reader(f)
        for row in reader:
            reader_dict.append(row)
    reader_dict.pop(0)
    return reader_dict



conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="12345"
)
try:
    with conn:
        with conn.cursor() as cur:
            for customer in rm_file(('customers_data.csv')):
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (customer[0], customer[1], customer[2]))
                cur.execute("SELECT * FROM customers")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
finally:
    conn.close()



try:
    with conn:
        with conn.cursor() as cur:
            for employee in rm_file(('employees_data.csv')):
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
                cur.execute("SELECT * FROM employees")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
finally:
    conn.close()



try:
    with conn:
        with conn.cursor() as cur:
            for order in rm_file(('orders_data.csv')):
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (order[0], order[1], order[2], order[3], order[4]))
                cur.execute("SELECT * FROM orders")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
finally:
    conn.close()