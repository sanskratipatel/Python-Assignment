def validate_user(user):
    # Ensure name is not empty and email contains '@'
    return len(user[1]) > 0 and "@" in user[2]

def validate_product(product):
    # Ensure price is positive
    return product[2] > 0

def validate_order(order, users, products):
    # Ensure quantity is positive, and user_id/product_id exist
    user_ids = {u[0] for u in users}
    product_ids = {p[0] for p in products}
    return order[3] > 0 and order[1] in user_ids and order[2] in product_ids
