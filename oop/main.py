class QuickBiteRestaurant:

    def __init__(self):
        self.menu = {
            "B1": {"name": "Classic Burger", "price": 99.00},
            "B2": {"name": "Cheese Burger", "price": 119.00},
            "C1": {"name": "Chicken Meal", "price": 149.00},
            "F1": {"name": "French Fries", "price": 59.00},
            "P1": {"name": "Pizza Slice", "price": 89.00},
            "D1": {"name": "Soft Drink", "price": 49.00},
            "D2": {"name": "Iced Tea", "price": 45.00},
            "S1": {"name": "Ice Cream", "price": 69.00}
        }

        self.orders = {}

    def display_menu(self):
        print("\n" + "=" * 50)
        print("              QUICK BITE RESTAURANT")
        print("=" * 50)
        print(f"{'CODE':<8}{'MENU ITEM':<25}{'PRICE':>10}")
        print("-" * 50)

        for code, item in self.menu.items():
            print(
                f"{code:<8}"
                f"{item['name']:<25}"
                f"₱{item['price']:>8.2f}"
            )

        print("=" * 50)

    def get_order_choice(self):
        while True:
            choice = input(
                "\nWould you like to order? (yes/no): "
            ).strip().lower()

            if choice in ["yes", "y"]:
                return True
            elif choice in ["no", "n"]:
                return False

            print("Invalid input. Please enter yes or no.")

    def get_menu_item(self):
        while True:
            code = input("\nEnter the menu code: ").strip().upper()

            if code in self.menu:
                return code

            print("Invalid menu code. Please choose an item from the menu.")

    def get_quantity(self):
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    return quantity

                print("Quantity must be greater than zero.")

            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def add_order(self, code, quantity):
        if code in self.orders:
            self.orders[code]["quantity"] += quantity
        else:
            self.orders[code] = {
                "name": self.menu[code]["name"],
                "price": self.menu[code]["price"],
                "quantity": quantity
            }

    def ask_for_another_order(self):
        while True:
            choice = input(
                "\nWould you like to order another item? (yes/no): "
            ).strip().lower()

            if choice in ["yes", "y"]:
                return True
            elif choice in ["no", "n"]:
                return False

            print("Invalid input. Please enter yes or no.")

    def calculate_total(self):
        subtotal = 0

        for item in self.orders.values():
            subtotal += item["price"] * item["quantity"]

        discount = 0

        if subtotal >= 500:
            discount = subtotal * 0.10

        total = subtotal - discount

        return subtotal, discount, total

    def print_receipt(self, subtotal, discount, total):
        print("\n\n" + "=" * 60)
        print("                 QUICK BITE RESTAURANT")
        print("                    OFFICIAL RECEIPT")
        print("=" * 60)

        print(f"{'ITEM':<22}{'QTY':>6}{'PRICE':>14}{'TOTAL':>14}")
        print("-" * 60)

        for item in self.orders.values():
            item_total = item["price"] * item["quantity"]

            print(
                f"{item['name']:<22}"
                f"{item['quantity']:>6}"
                f"₱{item['price']:>12.2f}"
                f"₱{item_total:>12.2f}"
            )

        print("-" * 60)
        print(f"{'SUBTOTAL':>45} ₱{subtotal:>10.2f}")
        print(f"{'DISCOUNT':>45} ₱{discount:>10.2f}")
        print(f"{'TOTAL':>45} ₱{total:>10.2f}")
        print("=" * 60)
        print("             Thank you for ordering!")
        print("                  Please come again!")
        print("=" * 60)

    def run(self):
        self.display_menu()

        if not self.get_order_choice():
            print("\nThank you for visiting Quick Bite Restaurant!")
            print("Have a great day!")
            return

        while True:
            self.display_menu()

            code = self.get_menu_item()
            quantity = self.get_quantity()

            self.add_order(code, quantity)

            print("\nItem successfully added to your order!")

            if not self.ask_for_another_order():
                break

        subtotal, discount, total = self.calculate_total()

        self.print_receipt(subtotal, discount, total)


restaurant = QuickBiteRestaurant()
restaurant.run()