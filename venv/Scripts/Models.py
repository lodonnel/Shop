class Item:

    # python can only have a single constructor
    def __init__(self, **kwargs):
        # if len(args) > 0:
        #     self._name = args[0]
        #     self._stock = args[1]
        #     self._price = args[2]
        if len(kwargs) > 0:
            self._stock = int(kwargs["stock"])
            self._name = kwargs["name"]
            self._price = float(kwargs["price"])

        else:  # empty constructor
            self._stock = 0
            self._name = ""
            self._price = 0.0

    # getters/setters
    def stock(self, value=None):
        if value is None:
            return self._stock
        else:
            self._stock = value

    def name(self, new_name=None):
        if new_name is None:
            return self._name
        else:
            self._name = new_name

    def price(self, new_price=None):
        if new_price is None:
            return self._price
        else:
            self._price = new_price


class Food(Item):

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            if len(args) == 1:  # csv line
                args = args[0].split(',')
            list_items = {}

            for k, v in args:
                list_items[k] = v

            super().__init__(**list_items)
            self._weight = args[3]
        elif len(kwargs) > 0:

            super().__init__(**kwargs)
            self._weight = kwargs["weight"]
        else:
            super().__init__(args)
            self._weight = args[3]

    def from_csv(self, **kwargs):
        pass

    def food_from_csv(self, food_list):
        pass

    def drink_from_csv(self, drink_list):
        pass

    def list_for_table(self):
        return [ self.name(), f'€{self.price()}', self.stock(), f'{self.weight()} gm']

    def to_csv(self):
        return f'name:{self.name()},stock:{self.stock()},price:{self.price()},weight:{self.weight()}'

    def weight(self, weight=None):
        if weight is None:
            return self._weight
        else:
            self._weight = weight

    def to_csv_kwargs(self):
        return f'name:{self.name()},price:{self.price()},' \
               f'stock:{self.stock()},weight:{self.weight()}'


class Drink(Item):

    def __init__(self, *args, **kwargs):

        if len(args) > 0:
            if len(args) == 1:  # csv line
                args = args[0].split(',')
            list_items = {}

            for k, v in args:
                list_items[k] = v

            super().__init__(**list_items)
            self._size = args[3]
        elif len(kwargs) > 0:

            super().__init__(**kwargs)
            self._size = kwargs["size"]
        # else:
        #     super().__init__(args)
        #     self._size = args[3]

    def size(self, size=None):
        if size is None:
            return self._size
        else:
            self._size = size

    def to_csv(self):
        return f'name:{self.name()},price:{self.price()},' \
               f'stock:{self.stock()},size:{self.size()}'

    def list_for_table(self):
        return [ self.name(), f'€{self.price()}', self.stock(), f'{self.size()} ml']


class CartItem(Item):
    pass

# if __name__ == '__main__': main()
