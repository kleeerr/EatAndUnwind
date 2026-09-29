class Restaurant:

    def __init__(self):

        self.menu = {
            "1": ("Chicken Burger", 85.00),
            "2": ("Cheeseburger", 95.00),
            "3": ("French Fries", 50.00),
            "4": ("Chicken Nuggets", 75.00),
            "5": ("Spaghetti", 65.00),
            "6": ("Fried Chicken", 90.00),
            "7": ("Soft Drink", 35.00),
            "8": ("Iced Tea", 40.00)
        }

        self.orders = []


    def display_menu(self):

        print()
        print("=" * 48)
        print(" " * 15 + "EAT AND UNWIND")
        print(" " * 15 + "FAST FOOD MENU")
        print("=" * 48)

        print(f"{'NO.':<6}{'MENU ITEM':<25}{'PRICE':>17}")
        print("-" * 48)

        for number, item in self.menu.items():

            name, price = item
            price_text = "PHP " + format(price, ".2f")

            print(
                f"{number:<6}"
                f"{name:<25}"
                f"{price_text:>17}"
            )

        print("=" * 48)


    def get_yes_no(self, question):

        while True:

            answer = input(question).strip().upper()

            if answer == "Y":
                return True

            elif answer == "N":
                return False

            else:
                print("\nInvalid input!")
                print("Please enter Y for Yes or N for No.")


    def get_menu_choice(self):

        while True:

            choice = input("\nEnter menu number: ").strip()

            if choice in self.menu:
                return choice

            else:
                print("\nInvalid menu number!")
                print("Please choose a number from the menu.")


    def get_quantity(self):

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


    def take_order(self):

        while True:

            choice = self.get_menu_choice()

            name, price = self.menu[choice]

            quantity = self.get_quantity()

            order = {
                "name": name,
                "quantity": quantity,
                "price": price
            }

            self.orders.append(order)

            print("\n" + "-" * 48)
            print(f"{quantity} x {name} added to your order.")
            print("-" * 48)

            another_item = self.get_yes_no(
                "\nWould you like to order another item? (Y/N): "
            )

            if not another_item:
                break


    def calculate_total(self):

        subtotal = 0

        for order in self.orders:

            item_total = order["quantity"] * order["price"]

            subtotal += item_total

        return subtotal


    def calculate_discount(self, subtotal):

        if subtotal >= 500:
            discount = subtotal * 0.10
        else:
            discount = 0

        return discount


    def print_receipt(self):

        subtotal = self.calculate_total()

        discount = self.calculate_discount(subtotal)

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

        for order in self.orders:

            item_name = order["name"]
            quantity = order["quantity"]

            item_total = (
                order["quantity"] *
                order["price"]
            )

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


    def run(self):

        print("\n")
        print("=" * 48)
        print(" " * 19 + "WELCOME TO")
        print(" " * 12 + "EAT AND UNWIND RESTAURANT")
        print("=" * 48)

        self.display_menu()

        wants_to_order = self.get_yes_no(
            "\nWould you like to order? (Y/N): "
        )

        if not wants_to_order:

            print()
            print("=" * 48)
            print(" " * 9 + "Thank you for visiting Eat and Unwind!")
            print(" " * 17 + "Have a great day!")
            print("=" * 48)

            return

        self.take_order()

        self.print_receipt()


restaurant = Restaurant()

restaurant.run()