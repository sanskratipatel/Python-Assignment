from database_setup import setup_databases
from data import users_data, products_data, orders_data
from validation import validate_user, validate_product, validate_order
import sqlite3

def insert_data(db_name, table_name, data):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        try:
            placeholders = ", ".join(["?"] * len(data[0]))
            cursor.executemany(f"INSERT OR IGNORE INTO {table_name} VALUES ({placeholders})", data)
            conn.commit()
            print(f"Inserted into {table_name} successfully")
        except Exception as e:
            print(f"Error inserting into {table_name}: {e}")

def remove_duplicates(data):
    unique_ids = set()
    unique_data = []
    for record in data:
        if record[0] not in unique_ids:
            unique_ids.add(record[0])
            unique_data.append(record)
    return unique_data

def fetch_data(db_name, table_name):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall()

if __name__ == "__main__":
    # Step 1: Setup databases
    setup_databases()

    # Step 2: Validate data and remove duplicates
    valid_users = [u for u in remove_duplicates(users_data) if validate_user(u)]
    valid_products = [p for p in remove_duplicates(products_data) if validate_product(p)]
    valid_orders = [o for o in remove_duplicates(orders_data) if validate_order(o, valid_users, valid_products)]

    # Step 3: Insert data into tables
    insert_data("users.db", "Users", valid_users)
    insert_data("products.db", "Products", valid_products)
    insert_data("orders.db", "Orders", valid_orders)

    # Step 4: Fetch and display data
    print("Users:", fetch_data("users.db", "Users"))
    print("Products:", fetch_data("products.db", "Products"))
    print("Orders:", fetch_data("orders.db", "Orders"))
