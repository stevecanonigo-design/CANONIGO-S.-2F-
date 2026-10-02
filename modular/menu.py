def display_menu(menu):
    print("\n" + "=" * 50)
    print("              QUICK BITE RESTAURANT")
    print("=" * 50)
    print(f"{'CODE':<8}{'MENU ITEM':<25}{'PRICE':>10}")
    print("-" * 50)

    for item_code, item_details in menu.items():
        print(
            f"{item_code:<8}"
            f"{item_details['name']:<25}"
            f"₱{item_details['price']:>8.2f}"
        )

    print("=" * 50)


def get_menu_item(menu):
    while True:
        item_code = input("\nEnter the menu code: ").strip().upper()

        if item_code in menu:
            return item_code

        print("Invalid menu code. Please choose an item from the menu.")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                return quantity

            print("Quantity must be greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")