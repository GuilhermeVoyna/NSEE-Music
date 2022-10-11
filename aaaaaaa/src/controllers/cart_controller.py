from src.models.cart import Cart

class CartController():
    def __init__(self):
        self._cart = Cart()
    def get_cart(self):
        return self._cart
    def add_product(self,product,quantity):
        for i in range(len(self.get_cart().get_products())):
            if self._cart.get_products()[i][0].get_name() == product.get_name():
                self._cart.get_products()[i][1] += quantity
                return
        self._cart._products.append([product,quantity])

    def get_total_price(self):
        total = 0
        for items in self._cart.get_products():
            total += items[0].get_price() * items[1]
        return total