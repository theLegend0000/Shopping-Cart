from designing import star_print, text


class Store:

  def __init__(self):  #method overriding
    self.products = []

  def add_products(self, product):
    self.products.append(product)

  def update_stock(self, product_name, stock):

    with open('quantity.txt', 'w') as f:
      pass          # this empties the content of 'quantity.txt' file before writing the new stock value

    with open('quantity.txt', 'a+') as f:
      f.seek(0)
      # Iterate over the products in self.products
      for item in self.products:
        # Check if the current product's name matches the one being updated
        if item.get_name() == product_name:
          f.write(f"ID: {item.get_productID()}, Name: {item.get_name()}, Price: {item.get_price()}, Quantity: {stock}\n")
        else:
          # Write the stock for the other products
          f.write(f"ID: {item.get_productID()}, Name: {item.get_name()}, Price: {item.get_price()}, Quantity: {item.get_stock()}\n")

  def view_products(self):
    star_print('PRODUCT LIST',27)

    print('\n')
    for _ in range(55):
      text('_', delay=0.001, end='')
    text(
        f"\n{'ProductID |':<14}{'Name':<11} {'|':<4}{'Price':<9} {'|':<5}{'Quantity':<8} {'|'}",
        delay=0.001)
    for _ in range(55):
      if _ == 10:
        text('|', delay=0.001, end='')
        continue
      if _ == 26:
        text('|', delay=0.001, end='')
        continue

      if _ == 40:
        text('|', delay=0.001, end='')
        continue

      if _ == 54:
        text('|', delay=0.001, end='')
        continue
      text('_', delay=0.001, end='')
    print()
    for items in self.products:
      text(
          f"{items.get_productID():<9} {'|':<4}{items.get_name():<11} {'|':<4}{items.get_price():<5} {'Rs'}  {'|':<5}{items.get_stock():<8} {'|'}",
          delay=0.001)
    for _ in range(55):
      if _ == 10:
        text('|', delay=0.001, end='')
        continue
      if _ == 26:
        text('|', delay=0.001, end='')
        continue

      if _ == 40:
        text('|', delay=0.001, end='')
        continue

      if _ == 54:
        text('|', delay=0.001, end='')
        continue
      text('_', delay=0.001, end='')
    print('\n')

  def get_product_names(self):
    product_names = []
    for item in self.products:
      product_names.append(item.get_name())
    return product_names
    
  def get_product_IDs(self):
    product_IDs = []
    for item in self.products:
      product_IDs.append(item.get_productID())
    return product_IDs