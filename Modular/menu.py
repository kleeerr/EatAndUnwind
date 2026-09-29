def display_menu(menu):

    print()
    print("=" * 48)
    print(" " * 15 + "EAT AND UNWIND")
    print(" " * 15 + "FAST FOOD MENU")
    print("=" * 48)

    print(f"{'NO.':<6}{'MENU ITEM':<25}{'PRICE':>17}")
    print("-" * 48)

    for number, item in menu.items():

        name, price = item
        price_text = "PHP " + format(price, ".2f")

        print(
            f"{number:<6}"
            f"{name:<25}"
            f"{price_text:>17}"
        )

    print("=" * 48)


def get_menu():

    menu = {
        "1": ("Chicken Burger", 85.00),
        "2": ("Cheeseburger", 95.00),
        "3": ("French Fries", 50.00),
        "4": ("Chicken Nuggets", 75.00),
        "5": ("Spaghetti", 65.00),
        "6": ("Fried Chicken", 90.00),
        "7": ("Soft Drink", 35.00),
        "8": ("Iced Tea", 40.00)
    }

    return menu