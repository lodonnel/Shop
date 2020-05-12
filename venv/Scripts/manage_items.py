import Display
from Models import Food
from Models import Drink
from Models import Item

from prettytable import PrettyTable


class ManageItems:
    items = {}

    def add(self, item):
        pass

    def delete(self, item):
        pass

    def update(self, item):
        pass

    def add_all(self, lines, item_type):
        food_count = 0
        drink_count = 0

        for line in lines:
            line["stock"] = int(line["stock"])
            line["price"] = float(line["price"])
            if item_type == "food":
                food = Food(**line)
                self.items[food.name().lower()] = food
                food_count += 1
            else:
                drink = Drink(**line)
                self.items[drink.name().lower()] = drink
                drink_count += 1
        print(f'Food Items added: {food_count}')
        print(f'Drink Items added: {drink_count}')

        # elif item_type == "ShoppingCart":
        #     for line in lines:
        #         cart_item = CartItem(line)
        #         self.items[cart_item.name()] = cart_item
        #     print(f'Shopping Cart Items added: {count}')
        #
        # else:   # must be transactions
        #     for line in lines:
        #         print(line)
        #     print(f'Transactions added: {count}')

    def list_items(self, item_type):
        products = []

        if item_type == "food":
            for item in self.items:
                if item is Food:
                    products.append(item.to_csv())
        else:
            for item in self.items:
                if item is Drink:
                    products.append(item.to_csv())

        return products

    def add_food(self):
        pass

    def add_drink(self):
        pass

    def add_stock(self):
        pass

    def list_food(self):
        food_items = []
        for item in self.items:
            if item is Food:
                food_items.append(item.list_for_table())
        Display.table_to_console(self.table_header(), food_items)

    def list_drink(self):
        drink_items = []
        for key in self.items:
            obj = self.items[key]
            if type(obj) == type(Drink()):
                table_row = obj.list_for_table()
                drink_items.append(table_row)
        Display.table_to_console(self.table_header(), drink_items)

    def table_header(self):
        return ["Product Name", "Price", "Stock", "Size/Weight"]
