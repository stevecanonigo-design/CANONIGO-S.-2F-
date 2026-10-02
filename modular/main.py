from menu import display_menu, get_menu_item, get_quantity
from order import (
    get_order_choice,
    add_order,
    ask_for_another_order,
    calculate_total
)
from receipt import print_receipt


def main():

    menu = {
        "B1": {"name": "Classic Burger", "price": 99.00},
        "B2": {"name": "Cheese Burger", "price": 119.00},
        "C1": {"name": "Chicken Meal", "price": 149.00},
        "F1": {"name": "French Fries", "price": 59.00},
        "P1": {"name": "Pizza Slice", "price": 89.00},
        "D1": {"name": "Soft Drink", "price": 49.00},
        "D2": {"name": "Iced Tea", "price": 45.00},
        "S1": {"name": "Ice Cream", "price": 69.00}
    }

    orders = {}

    display_menu(menu)

    if not get_order_choice():
        print("\nThank you for visiting Quick Bite Restaurant!")
        print("Have a great day!")
        return

    while True:
        display_menu(menu)

        item_code = get_menu_item(menu)
        quantity = get_quantity()

        add_order(orders, menu, item_code, quantity)

        print("\nItem successfully added to your order!")

        if not ask_for_another_order():
            break

    subtotal, discount, total = calculate_total(orders)

    print_receipt(orders, subtotal, discount, total)


if __name__ == "__main__":
    main()