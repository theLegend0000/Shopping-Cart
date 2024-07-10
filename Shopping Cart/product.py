class Product:

  def __init__(self, name):  #method overriding
    self.name = name
    self.price = self.load_price()
    self.stock = self.load_stock()
    self.product_ID = self.load_ID()
  
  def get_name(self):
    return self.name
  
  def get_price(self):
    return self.price
  
  def get_stock(self):
    return self.stock

  def get_productID(self):
    return self.product_ID

  def load_ID(self):
    with open('quantity.txt') as f:
      for line in f:
        if self.get_name() in line:
          ID = line.split('ID:')[1].split(',')[0].strip()
          ID = int(ID)
          return ID
        

  def load_price(self):
    with open('quantity.txt') as f:
      for line in f:
        if self.get_name() in line:
          price = line.split('Price:')[1].split(',')[0].strip()
          price = int(price)
          return price

  def load_stock(self):
    with open('quantity.txt') as f:
      for line in f:
        if self.get_name() in line:
          stock = line.split('Quantity:')[1].strip()
          stock = int(stock)
          return stock