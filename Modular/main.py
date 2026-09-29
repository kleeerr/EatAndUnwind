from menu import get_menu, display_menu
from ordering import get_yes_no, get_order
from receipt import print_receipt


def main():

    menu = get_menu()

    print("\n")
    print("=" * 48)
    print(" " * 19 + "WELCOME TO")
    print(" " * 12 + "EAT AND UNWIND RESTAURANT")
    print("=" * 48)

    display_menu(menu)

    wants_to_order = get_yes_no(
        "\nWould you like to order? (Y/N): "
    )

    if not wants_to_order:

        print()
        print("=" * 48)
        print(" " * 9 + "Thank you for visiting Eat and Unwind!")
        print(" " * 17 + "Have a great day!")
        print("=" * 48)

        return

    orders = get_order(menu)

    print_receipt(orders)


main()