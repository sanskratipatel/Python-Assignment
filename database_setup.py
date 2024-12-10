import sqlite3

def initialize_database(db_name, create_table_query):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()

# Table creation queries
CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);
"""

CREATE_PRODUCTS_TABLE = """
CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
);
"""

CREATE_ORDERS_TABLE = """
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL
);
"""

def setup_databases():
    initialize_database("users.db", CREATE_USERS_TABLE)
    initialize_database("products.db", CREATE_PRODUCTS_TABLE)
    initialize_database("orders.db", CREATE_ORDERS_TABLE)

if __name__ == "__main__":
    setup_databases()
