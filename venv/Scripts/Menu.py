class Menu(object):
    prompt = "Enter Menu Choice"
    err_message_prefix = "Your choice must be between "
    minimum = 1

    def __init__(self, name):
        if name == "main":
            self.menu = ["1. Staff Menu",
                         "2. Customer Menu",
                         "3. Exit System",
                         ]
            self.maximum = len(self.menu)
            self.err_message = f'{self.err_message_prefix} {self.minimum} and {self.maximum}'
        elif name == "customer":
            self.menu = ["1. Buy Item",
                         "2. Add to Cart",
                         "3. Manage Cart",
                         "4.",
                         "5.",
                         "6. Return to Main Menu",
                         ]
            self.maximum = len(self.menu)
            self.err_message = f'{self.err_message_prefix} {self.minimum} and {self.maximum}'
        elif name == "staff":
            self.menu = ["1. New Food Item",
                         "2. New Drink Item",
                         "3. List Food",
                         "4. List Drink",
                         "5. Add Stock",
                         "6. Return to Main Menu",
                         ]
            self.maximum = len(self.menu)
            self.err_message = f'{self.err_message_prefix} {self.minimum} and {self.maximum}'
        elif name == "manage cart":
            self.menu = ["1. List Cart Items",
                         "2. Delete Cart Item",
                         "3. Change quantity",
                         "4. Clear Cart",
                         "5. Checkout",
                         "6. Return to Customer Menu",
                         ]
            self.maximum = len(self.menu)
            self.err_message = f'{self.err_message_prefix} {self.minimum} and {self.maximum}'
        self.title = f'{name.title()} Menu'

# if __name__ == '__main__': main()
