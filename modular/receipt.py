def print_receipt(orders, subtotal, discount, total):
    print("\n\n" + "=" * 60)
    print("                 QUICK BITE RESTAURANT")
    print("                    OFFICIAL RECEIPT")
    print("=" * 60)

    print(f"{'ITEM':<22}{'QTY':>6}{'PRICE':>14}{'TOTAL':>14}")
    print("-" * 60)

    for item in orders.values():
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