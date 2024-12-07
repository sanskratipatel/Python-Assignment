import sqlite3
import threading
from data import users_data, products_data, orders_data
from validation import validate_user, validate_product, validate_order
from database_setup import setup_databases

def insert_data(db_name, table_name, data):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        try:
            placeholders = ", ".join(["?"] * len(data[0]))
            cursor.executemany(f"INSERT INTO {table_name} VALUES ({placeholders})", data)
            conn.commit()
            print(f"Inserted into {table_name} successfully")
        except Exception as e:
            print(f"Error inserting into {table_name}: {e}")

# Threaded Insertion
def threaded_insertion(db_name, table_name, data, validation_func=None):
    if validation_func:
        data = [row for row in data if validation_func(row)]
    thread = threading.Thread(target=insert_data, args=(db_name, table_name, data))
    thread.start()
    return thread

# Main function
if __name__ == "__main__":
    setup_databases()

    # Insert Users, Products, and Orders concurrently
    user_thread = threaded_insertion("users.db", "Users", users_data, validate_user)
    product_thread = threaded_insertion("products.db", "Products", products_data, validate_product)
    order_thread = threaded_insertion("orders.db", "Orders", orders_data, 
                                      lambda o: validate_order(o, users_data, products_data))

    # Wait for threads to finish
    user_thread.join()
    product_thread.join()
    order_thread.join()

    # Fetch and display results
    def fetch_data(db_name, table_name):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            return cursor.fetchall()

    print("Users:", fetch_data("users.db", "Users"))
    print("Products:", fetch_data("products.db", "Products"))
    print("Orders:", fetch_data("orders.db", "Orders"))
