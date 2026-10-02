def get_order_choice():
    while True:
        choice = input(
            "\nWould you like to order? (yes/no): "
        ).strip().lower()

        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False

        print("Invalid input. Please enter yes or no.")


def add_order(orders, menu, item_code, quantity):
    item_name = menu[item_code]["name"]
    item_price = menu[item_code]["price"]

    if item_code in orders:
        orders[item_code]["quantity"] += quantity
    else:
        orders[item_code] = {
            "name": item_name,
            "price": item_price,
            "quantity": quantity
        }


def ask_for_another_order():
    while True:
        choice = input(
            "\nWould you like to order another item? (yes/no): "
        ).strip().lower()

        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False

        print("Invalid input. Please enter yes or no.")


def calculate_total(orders):
    subtotal = 0

    for item in orders.values():
        subtotal += item["price"] * item["quantity"]

    discount = 0

    if subtotal >= 500:
        discount = subtotal * 0.10

    total = subtotal - discount

    return subtotal, discount, total