from os import system
from time import sleep

from cart_item import CartItem
from designing import star_print, text, clear_screen


class ShoppingCart:

  def __init__(self):  #method overriding
    self.items = []

  def add_item(self, product, quantity):
    check = True
    for item in self.items:
      if item.product == product:
        item.quantity += quantity  #if same item is already present in the cart the only the quantity will be added to it's quantity
        check = False
    if check:
      self.items.append(CartItem(product, quantity))  #Association (Composition)
    
  def get_item(self, productID):
    for item in self.items:
      if item.product.product_ID == productID:
        return item
        
  def rem_item(self, productID, quantity):
    self.productID = productID
    item = self.get_item(productID)
    if item is not None and item.quantity >= quantity:
      item.quantity -= quantity
    if item is not None and item.quantity == 0:
      return (self.items.remove(item))



  def view_cart(self):
    if len(self.items) == 0:
      text("Your cart is empty\n")
      sleep(1.4)
      clear_screen()
      return

    total = 0
    star_print('Your Cart', 40)
    print('\n\n')
    for i, item in enumerate(self.items):
      text(
          f"{i+1}{'.':<4}Product ID: {item.product.get_productID()}\n{' ':<5}Product Name: {item.product.get_name()}\n{' ':<5}Product Quantity: {item.quantity}\n{' ':<5}Product Price: {item.product.get_price()}\n"
      )
      total += item.product.get_price() * item.quantity
    text(f"Total Bill (Rs): {total}")

  def empty_cart(self):
    if len(self.items) == 0:
      text("Your cart is empty.")
      return

    self.items = []
