from shopping_cart import ShoppingCart
from transaction_order import Order
from user import User


class Customer(User):

  def __init__(self, name):
    super().__init__()#method overriding
    self.name = name
    self.shopping_cart = ShoppingCart() #Association (composition)
    self.order = Order(self.shopping_cart.items)

  def add_to_cart(self, productID, quantity):
    self.shopping_cart.add_item(productID, quantity)

  def remove_item(self, product, quantity):
    self.shopping_cart.rem_item(product, quantity)

  def view_cart(self):
    self.shopping_cart.view_cart()

  def empty_cart(self):
    self.shopping_cart.empty_cart()
    
  def checkout(self):
    return self.order.checkout()



