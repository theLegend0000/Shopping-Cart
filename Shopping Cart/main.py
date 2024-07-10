from datetime import datetime, time
from os import mkdir, system
from time import sleep

from pytz import timezone

from admin import Administrator
from customer import Customer
from designing import clear_screen, star_print, text
from product import Product
from store import Store
from user import User

# Driver Code

# Initiating the Store

store = Store()

# Initiating the Products in the Store

with open('quantity.txt') as f:
  for line in f:
    name = line.split('Name:')[1].strip().split(',')[0]
    product = Product(name)  #  Creating Product
    store.add_products(product)  # Adding the product to the store
while True:  #prints the main text of the application
  star_print('WELCOME TO ONLINE SHOPPING CART', 23)
  text(
    '\n1. Create an account\n\n2. Sign In\n\n3. Admin Panel\n\n4. Exit\n\n')


  text('Select an option (from 1 to 4): ')
  choice = input()
  if choice == '2':
    clear_screen()

    star_print('Sign In', 23)
    temp = Customer(None)
     #creating a temporary customer object on which sign in or sign up will be performed
    data, username = temp.sign_in()
    if data is True:

      customer = Customer(username)  # creating the customer object
                                     # Customer enters the store and perform shopping actions
      break

    elif data is False:
      text('\nPress any key to continue...\n')
      choice = input()
      clear_screen()
      continue

  elif choice == '1':
    clear_screen()

    star_print('Create an account', 23)
    temp = Customer(None)
    # creating a temporary customer on which the sign up or sign up actions can be performed
    username = temp.sign_up()
    if username is None or username == 'continue':
      clear_screen()
      continue

    if username == 'exit':
      
      text('Thanks for visiting the store bye!')
      sleep(1)
      exit()


    customer = Customer(username)  # creates the customer object
                                   # Customer enters the store and perform shopping actions
    break

  elif choice == '3':
    admin = Administrator()
    clear_screen()
    star_print('Admin Panel', 23)
    print('\n')
    check, username = admin.sign_in()
    if check is True:
      sleep(1)
      clear_screen()
      while True:

        clear_screen()
        text(
            "\n1. View Customers' Details\n\n2. Delete Customer\n\n3. Add Product\n\n4. Update Stock\n\n5. Back to main menu\n"
        )

        choice = input()
        if choice == '1':
          clear_screen()
          admin.view_customers()
          text('Press any key to continue...')
          input()
        elif choice == '2':
          clear_screen()
          text('Enter the username of the customer you want to delete: ')
          d_username = input()
          admin.delete_customer(d_username)

        elif choice == '3':
          product_names = store.get_product_names()
          product_IDs = store.get_product_IDs()
          clear_screen()
          text(
              'Enter the name of the product you want to add (Enter 0 to Cancel): '
          )
          product_name = input().capitalize()
          if product_name == '0':
            text('Operation Cancelled')
            sleep(1.2)
            clear_screen()
            continue
          if product_name in product_names:
            text('Product already exists.')
            sleep(1.3)
            clear_screen()
            continue
          text('\nEnter the price of the product:')
          price = input()
          if price.isdigit():
            price = int(price)
            text('\nEnter the quantity of the product:')
            quantity = input()
            if quantity.isdigit():
              quantity = int(quantity)
              with open('quantity.txt', 'a+') as f:
                f.write(
                    f'\nID: {product_IDs[-1] + 1}, Name: {product_name}, Price: {price}, Quantity: {quantity}'
                )
              new_product = admin.add_product(product_name)
              store.add_products(new_product)
              text('Product Successfully Added to The Store.')
              sleep(1.3)
              clear_screen()
              continue
            else:
              text('Invalid Quantity. Please Enter a Valid Quantity.')
              sleep(1.3)
              clear_screen()
              continue
          else:
            text('Invalid Price. Please Enter a Valid Price.')
            sleep(1.3)
            clear_screen()
            continue
        elif choice == '4':
          clear_screen()
          text('Enter the name of the product whose stock you want to update: ')
          product_name = input().capitalize()
          product_names = store.get_product_names()
          if product_name  in product_names:
            text('Enter the new stock quantity: ')
            stock = input()
            if stock.isdigit():
              stock = int(stock)
              store.update_stock(product_name.capitalize(), stock)
              text('Stock updated successfully.')
              sleep(1)
              clear_screen()
              continue
            else:
              text('Invalid Stock. Please enter a valid integer.')
              sleep(1)
              clear_screen()
              continue
          else:
            text('Invalid product name. Please try again.')
            sleep(1)
            clear_screen()
            continue
        elif choice == '5':
          clear_screen()
          break

        else:
          text('Invalid choice. Please try again.\n')
          sleep(0.9)
          clear_screen()

    if check is False:
      sleep(1)
      clear_screen()
      continue


  elif choice == '4':
    text('Thank you for visiting the store. Good Bye!')
    sleep(1)
    exit()

  else:
    text('Invalid choice. Please try again.')
    sleep(1)
    clear_screen()
clear_screen()

while True:
  star_print('Main Menu', 25)

  # Displaying Menu

  text(
      '\n\n1. View Product List\n2. View Cart\n3. View Shopping History\n4. Exit\n'
  )
  choice = input()
  if choice == '1':
    clear_screen()
    store.view_products()
    while True:
      text('\n\n1. Add Product(s) to Cart\n2. Back to Main Menu\n Select an option (from 1 to 2): ')
      choice = input()
      if choice == '1':
        clear_screen()
        store.view_products()
        while True:
          text(
              'Enter the product number you want to add to cart: (0 to Cancel)'
          )
          product_number = input()  # take str input
          if product_number == '0':
            text('Operation cencelled.')
            sleep(1)
            clear_screen()
            break
          product_IDs = store.get_product_IDs()

          if product_number.isdigit() and int(product_number) in product_IDs:
            product_number = int(product_number)
            try:  #Exception Handling ('Index Error')
              product = store.products[product_number - 1]
            except IndexError:
              text('Invalid Product Number. Please try again.')
              continue
            else:
              text('Enter the quantity: ')
              quantity = input()
              # take str input
              if quantity.isdigit():
                quantity = int(quantity)
                if 0 < quantity <= product.get_stock():
                  customer.add_to_cart(product, quantity)
                  text(f'{quantity} {product.name} added to cart.')
                  stock = product.get_stock() - quantity
                  product.stock = stock
                  store.update_stock(product.name, stock)
                else:
                  text('Invalid Quantity. Please try again.')
                  continue
                text('Do you want to add more products? [y/n]')
                choice = input()
              else:
                text('Invalid quantity. Please try again.')
                continue

            if choice.lower() == 'n':
              clear_screen()
              break
            elif choice.lower() == 'y':
              clear_screen()
              store.view_products()
              print()
              pass
            else:
              text('Invalid choice. Please try again.')
          else:
            text('Invalid choice. Please try again.')

      elif choice == '2':
        clear_screen()
        break
      else:
        text('Invalid choice. Please try again.')

  elif choice == '2':
    clear_screen()
    customer.view_cart()
    if len(customer.shopping_cart.items) > 0:
      text('\n1. Remove items from the cart')
      text('2. Checkout')
      text('3. Back to the main menu')

      choice = input()
      if choice.lower() == '1':
        while True:

          text('\n\nEnter the product ID you want to remove from cart: ')
          product_id = input()
          if product_id.isdigit():
            product_id = int(product_id)
          else:
            text('Invalid Product ID. Please Try Again.')
            sleep(1)
            continue

          for item in customer.shopping_cart.items:
            if not (item.product.product_ID == product_id):
                text('Invalid Product ID.\n')
                sleep(1)
                continue
            else:
              try:

                product = item.product
                pro_quantity = item.quantity

              except IndexError:  #Exception Handling of 'IndexError'
                text('Invalid Product ID. Please Try Again.\n')
                sleep(2)
                continue
              else:
                text('Enter the quantity: ')
                quantity = input()

                if (quantity.isdigit()):
                  quantity = int(quantity)
                  if (quantity <= pro_quantity):
                    customer.remove_item(product_id, quantity)
                    text(f'{quantity} {product.name} removed from cart.')
                    sleep(1.5)
                  else:
                    text('Invalid Quantity. Please try again.')
                    sleep(1)
                else:
                  text('Invalid quantity. Please try again.')

          if len(customer.shopping_cart.items) == 0:
            text('\nYour cart is empty.\n\n')
            sleep(2)
            clear_screen()
            break

          else:
            clear_screen()
            customer.view_cart()
            text('\nDo you want to remove more items? [y/n]')
            choice = input()
            if choice.lower() == 'n':
              clear_screen()
              break
            elif choice.lower() == 'y':
              pass

      elif choice == '2':
        clear_screen()
        if customer.checkout() == 'successfull':
          path = 'user_data/customers_shopping_history'
          try:

            path = 'user_data/customers_shopping_history'
            mkdir(path)
          except FileExistsError:  #Error Handling of 'FileExistsError'
            pass
          finally:
            file_path = f'{path}/{customer.name}.txt'
            with open(file_path, 'a+') as f:
              f.seek(0)
              if customer.name in f.read().splitlines():
                pass
              else:
                f.write(f'Shopping History of {customer.name}\n\n')
              for item in customer.shopping_cart.items:
                f.write(f'Item Purchased: {item}\n')
                f.write(f'Quantity: {item.quantity}\n')
                time = datetime.now(timezone('Asia/Karachi'))
                f.write(
                    f'Purchased Date: {time.strftime("%y/%m/%d %H:%M")}\n\n')
            customer.empty_cart()
            for item in customer.shopping_cart.items:

              store.update_stock(item.get_name(), item.get_stock())
            
            while True:
              text('Do you want to...\n1. Continue Shopping\n2. Exit')
              choice = input()
              if choice == '1':
                clear_screen()
                break

              elif choice == '2':
                clear_screen()
                text('Thank you for shopping with us.')
                exit()
              else:
                text('Invalid choice. Please try again.')
                sleep(1)
                clear_screen()
                continue

      elif choice == '3':
        clear_screen()

      else:
        text('Invalid Choice. Please try again.')
        sleep(1)
        clear_screen()

  elif choice == '3':
    clear_screen()
    try:
      file_path = f'user_data/customers_shopping_history/{username}.txt'
      with open(file_path, 'r') as f:
        shopping_history = f.read()
    except FileNotFoundError:  #try exception block of 'FileNotFoundError'
      text('No shopping history found.')
      sleep(1.4)
      clear_screen()
    else:
      star_print('Shopping History', 50)
      text(shopping_history + '\n')
      text('1. Back to Main Menu')
      choice = input()
      if choice == '1':
        clear_screen()
      else:
        text('Invalid choice. Please try again.')

  elif choice == '4':
    text('Thanks for visiting the store.\nHave a nice day!')
    sleep(1)
    break
  else:
    text('Invalid Input')
    sleep(1.4)
    clear_screen()
