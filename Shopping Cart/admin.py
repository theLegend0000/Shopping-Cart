import os
from time import sleep

from designing import random_color_star_print, text
from product import Product
from user import User


class Administrator(User):  #Inheritance

    def __init__(self):    #method ovirriding
      super().__init__()
      self.username = "admin"  # Assign default username for admin
      self.password = "admin"  # Assign default password for admin
    
    def sign_in(self):
      text('Enter your username:')
      username = input()
      random_color_star_print(23)
      text('Enter your password: ')
      password = input()
      random_color_star_print(23)
      if username == self.username and password == self.password:
          text("Sign-in successful.")
          return True, username
      else:
          text("Invalid username or password.")
          return False, username
    
    def view_customers(self):
      customer_folder = os.path.join(self.user_data_folder, "customers_info")
      if not os.path.exists(customer_folder):
          text("No customer data available.")
          sleep(1)
          return
      customer_files = [
          file for file in os.listdir(customer_folder)
          if file.endswith(".txt")
      ]
      if customer_files:
          text("List of customers:")
          for filename in customer_files:
              username = filename.split('.')[
                  0]  # Extract username from filename
              text(username,delay=0.07)
              
      else:
          text("No customers found.")
    

    import os

    def delete_customer(self, username):
        customer_folder = os.path.join(self.user_data_folder, "customers_info")
        shopping_history_folder = os.path.join(self.user_data_folder, "customers_shopping_history")

        if not os.path.exists(customer_folder):
            text("No customer data available.")
            sleep(1)
            return

        # Delete customer file
        customer_file = os.path.join(customer_folder, f"{username}.txt")
        if os.path.exists(customer_file):
            os.remove(customer_file)
            text(f"Account '{username}' has been deleted.")
            sleep(1)
        else:
            text(f"Account '{username}' not found.")
            sleep(1)
            return

        # Remove username from usernames.txt
        usernames_file = "usernames.txt"
        if os.path.exists(usernames_file):
            with open(usernames_file, "r") as file:
                lines = file.readlines()
            with open(usernames_file, "w") as file:
                for line in lines:
                    if line.strip() != username:
                        file.write(line)
            text(f"Username '{username}' has been removed from usernames.txt.")
            sleep(1)
        else:
            text("usernames.txt file not found.")
            
        # Delete customer's shopping history
        shopping_history_file = os.path.join(shopping_history_folder, f"{username}.txt")
        if os.path.exists(shopping_history_file):
            try:
                os.remove(shopping_history_file)
                text(f"Shopping history for '{username}' has been deleted.")
            except Exception as e:
                text(f"An error occurred while deleting the shopping history: {e}")
        else:
            text(f"Shopping history for '{username}' not found.")


    
    def view_customer_details(self, username):
      customer_folder = os.path.join(self.user_data_folder, "customers_info")
      customer_file = os.path.join(customer_folder, f"{username}.txt")
      if os.path.exists(customer_file):
          with open(customer_file, "r") as file:
              customer_details = file.read()
          text(f"Account details for '{username}':")
          text(customer_details)
      else:
          text(f"Account '{username}' not found.")

    def add_product(self, product_name):
        return Product(product_name)
    
