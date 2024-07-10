class CartItem:

  def __init__(self, product, quantity):  #method overriding
    self.product = product
    self.quantity = quantity

  def __str__(self):    #method Overriding
    return f'{self.product.get_name()}'