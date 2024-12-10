def validate_user(user):
    if not user[1]:  # Name cannot be empty
        print(f"Invalid User: {user} (Empty name)")
        return False
    return True

def validate_product(product):
    if product[2] < 0:  # Price cannot be negative
        print(f"Invalid Product: {product} (Negative price)")
        return False
    return True

def validate_order(order, users, products):
    user_ids = {u[0] for u in users}
    product_ids = {p[0] for p in products}
    if order[3] <= 0:  # Quantity must be positive
        print(f"Invalid Order: {order} (Invalid quantity)")
        return False
    if order[1] not in user_ids:
        print(f"Invalid Order: {order} (User ID not found)")
        return False
    if order[2] not in product_ids:
        print(f"Invalid Order: {order} (Product ID not found)")
        return False
    return True
