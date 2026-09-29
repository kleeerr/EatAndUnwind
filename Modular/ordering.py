def get_yes_no(question):

    while True:

        answer = input(question).strip().upper()

        if answer == "Y":
            return True

        elif answer == "N":
            return False

        else:
            print("\nInvalid input!")
            print("Please enter Y for Yes or N for No.")


def get_menu_choice(menu):

    while True:

        choice = input("\nEnter menu number: ").strip()

        if choice in menu:
            return choice

        else:
            print("\nInvalid menu number!")
            print("Please choose a number from the menu.")


def get_quantity():

    while True:

        quantity = input("Enter quantity: ").strip()

        try:

            quantity = int(quantity)

            if quantity > 0:
                return quantity

            else:
                print("\nQuantity must be greater than 0.")

        except ValueError:

            print("\nInvalid quantity!")
            print("Please enter a whole number.")


def get_order(menu):

    orders = []

    while True:

        choice = get_menu_choice(menu)

        name, price = menu[choice]

        quantity = get_quantity()

        order = {
            "name": name,
            "quantity": quantity,
            "price": price
        }

        orders.append(order)

        print("\n" + "-" * 48)
        print(f"{quantity} x {name} added to your order.")
        print("-" * 48)

        another_item = get_yes_no(
            "\nWould you like to order another item? (Y/N): "
        )

        if not another_item:
            break

    return orders