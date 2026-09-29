def calculate_total(orders):

    subtotal = 0

    for order in orders:

        item_total = order["quantity"] * order["price"]
        subtotal += item_total

    return subtotal


def calculate_discount(subtotal):

    if subtotal >= 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    return discount


def print_receipt(orders):

    subtotal = calculate_total(orders)
    discount = calculate_discount(subtotal)
    total = subtotal - discount

    width = 48

    print("\n")
    print("=" * width)
    print(" " * 15 + "EAT AND UNWIND")
    print(" " * 15 + "FAST FOOD RESTAURANT")
    print("-" * width)
    print(" " * 19 + "RECEIPT")
    print("-" * width)

    print()

    print(f"{'ITEM':<22}{'QTY':>6}{'TOTAL':>20}")
    print("-" * width)

    for order in orders:

        item_name = order["name"]
        quantity = order["quantity"]
        item_total = order["quantity"] * order["price"]

        print(
            f"{item_name:<22}"
            f"{quantity:>6}"
            f"{'PHP ' + format(item_total, '.2f'):>20}"
        )

    print()
    print("-" * width)

    print(
        f"{'Subtotal':<28}"
        f"{'PHP ' + format(subtotal, '.2f'):>20}"
    )

    if discount > 0:

        print(
            f"{'Discount (10%)':<28}"
            f"{'-PHP ' + format(discount, '.2f'):>20}"
        )

    else:

        print(
            f"{'Discount':<28}"
            f"{'PHP 0.00':>20}"
        )

    print("-" * width)

    print(
        f"{'TOTAL':<28}"
        f"{'PHP ' + format(total, '.2f'):>20}"
    )

    print("=" * width)

    print()
    print(" " * 15 + "THANK YOU!")
    print(" " * 11 + "Please come again!")
    print()
    print("       EAT AND UNWIND • GOOD FOOD • GOOD MOOD")
    print("=" * width)