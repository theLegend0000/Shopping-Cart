from time import sleep

from designing import text


class Transaction:

  def __init__(self,items):  #method overriding
    self.items = items

  def calculate_total(self):
    total_price = 0
    for item in self.items:
      total_price += item.product.get_price() * item.quantity
    return total_price


class Order(Transaction):  #Inheritance

  def __init__(self, items):  #method overriding
    super().__init__(items)

  def checkout(self):
    total_price = self.calculate_total()
    text("Checking out...")
    text(f"Total Price: Rs {total_price}")
    text("Do you want to proceed with the checkout? (y/n)")
    while True:
      choice = input()
      if choice.lower() == 'y':
        text('\nChecking out...')
        sleep(2)
        text("\nThank you for shopping with us!\nHave a great day!\n")

        return 'successfull'
      elif choice.lower() == 'n':
        text("Checkout cancelled.")
        return 'cancelled'
      else:
        text("Invalid choice. Please enter 'y' or 'n'.")
