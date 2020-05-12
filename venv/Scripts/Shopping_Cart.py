class ShoppingCart:
    cart_items = {}

    def add(self, product):
        if len(self.cart_items) > 0:
            if self.cart_items.keys().__contains__(product.get_name()):  # existing item
                # add stock value
                self.update_stock(product.stock())
            else:  # new item
                self.cart_items[product.name()] = product
        else:  # empty list
            self.cart_items[product.get_name()] = product

    def update(self):
        pass

    def update_stock(self, product):
        qty = product.quantity()
        old_qty = self.cart_items[product.name()].quantity()
        self.cart_items[product.name()].stock(qty + old_qty)

    def delete(self):
        pass

    def add_all(self, param, param1):
        pass
