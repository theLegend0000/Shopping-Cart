import hashlib
import os
import string
from time import sleep

from designing import clear_screen, random_color_star_print, star_print, text


class User:

    def __init__(self):    #method overriding
        self.user_data_folder = "./user_data"
        self.name = ""
        self.email = ""
        self.phone_no = ""
        self.username = None
        self.password = None

    @staticmethod
    def hash_password(password):
        """
        This function returns the SHA-256 hash of the password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def sign_in(self):
        text('Enter your username:')
        username = input()
        if username == '':
            text('Inavlid Username')
            return False, username
        random_color_star_print(23)
        text('Enter your password:')
        password = input()
        random_color_star_print(23)

        hashed_password = self.hash_password(password)

        user_file_path = os.path.join(self.user_data_folder, "customers_info",
                                      f"{username}.txt")

        if os.path.exists(user_file_path):
            with open(user_file_path, "r") as file:
                user_data = file.read().splitlines()
                stored_username = user_data[3].split(": ")[1]
                stored_password = user_data[4].split(": ")[1]

                if stored_username == username and stored_password == hashed_password:
                    text("Sign-in successful.")
                    random_color_star_print(23)
                    return True, username
                else:
                    text("Invalid username or password.")
                    random_color_star_print(23)
                    return False, username
        else:
            text("Invalid username or password.")
            random_color_star_print(23)
            return False, username

    def check_phone_no(self):
        text('Enter your phone number:')
        phone_no = input()
        random_color_star_print(23)

        while not phone_no.isdigit():
            text("Invalid phone number.\nPlease enter a valid phone number.")
            random_color_star_print(23)
            text('Enter your phone number:')
            phone_no = input()
            random_color_star_print(23)

        return int(phone_no)

    def generate_unique_username(self, name, file_path):
        try:
            base_username = name.lower().split()[0] + "_"
        except IndexError:
            return None
        else:
            username = base_username

            if not os.path.exists(file_path):
                with open(file_path, "w"):
                    pass

            with open(file_path, "r") as file:
                taken_usernames = set(file.read().splitlines())

            suffix = 1
            while username in taken_usernames:
                username = f"{base_username}{suffix}"
                suffix += 1

            return username

    def prompt_for_custom_username(self, file_path):
        text(f'Your default username is {self.username}.')
        random_color_star_print(23)
        text('Do you want to change it? [yes/no]')
        random_color_star_print(23)
        response = input().lower()
        if response == "yes":
            while True:
                random_color_star_print(23)
                text('Enter your desired username:')
                random_color_star_print(23)
                custom_username = input()
                random_color_star_print(23)
                with open(file_path, "r") as file:
                    taken_usernames = set(file.read().splitlines())
                if custom_username not in taken_usernames:
                    self.username = custom_username
                    break
                else:
                    text(
                        "Username is already taken.\nPlease choose a different one."
                    )
                    random_color_star_print(23)

    def prompt_for_password(self):
        while True:
            text('Enter your password:')
            password = input()
            random_color_star_print(23)
            if self.is_strong_password(password):
                return password
            else:
                text("- Password must be at least 8 characters long.\n- Must contain at least one uppercase letter.\n- Must contain at least one lowercase letter.\n- Must contain at least one digit.\n- Must contain at least one special character.")
                random_color_star_print(23)

    def is_strong_password(self, password):
        if len(password) < 8:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char in string.punctuation for char in password):
            return False
        return True

    def save_username_to_file(self, file_path):
        with open(file_path, "a") as file:
            file.write(f"{self.username}\n")
        text("Username has been successfully saved.")
        print()

    def save_to_file(self, folder_path):
        user_type_folder = "customers_info" if isinstance(
            self, User) else "administrators"
        folder_path = os.path.join(folder_path, user_type_folder)

        hashed_password = self.hash_password(self.password)
        user_data = f"Name: {self.name}\nPhone Number: {self.phone_no}\nEmail: {self.email}\nUsername: {self.username}\nPassword: {hashed_password}"

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        filename = os.path.join(folder_path, f"{self.username}.txt")

        with open(filename, "w") as file:
            file.write(user_data)

        text("Data have been successfully saved. \U0001F600")
        random_color_star_print(23)
        sleep(1)

    def sign_up(self):
        while True:
            text('Enter your name: (Press 0 to Cancel)')
            self.name = input()
            if self.name == '0':
                random_color_star_print(23)
                text('Sign-up cancelled.')
                sleep(1)
                return
            if self.name == '' or self.name.isdigit() :
               text('Invalid name. Do you want to continue? (y/n)')
               choice = input().lower()
               if choice == 'y':
                 clear_screen()
                 star_print('Create an account', 23)
                 continue
               elif choice == 'n':
                return 'continue'

 
            #     random_color_star_print(23)
            #     continue
            # random_color_star_print(23)

            while True:
                text('Enter your email:')
                self.email = input()
                random_color_star_print(23)
                if self.email.strip() == '':
                    text('Invalid email. Please enter a valid email.')
                    random_color_star_print(23)
                    continue
                if self.email != '' and self.email.count('@') >= 1 and self.email.count('.') == 1:
                    break
                else:
                    text('Invalid Email.\nPlease enter a valid email.')
                    random_color_star_print(23)

            self.phone_no = self.check_phone_no()
            self.username = self.generate_unique_username(
                self.name,
                "usernames.txt"
            )
 
            self.prompt_for_custom_username("usernames.txt")
            self.password = self.prompt_for_password()
            self.save_username_to_file("usernames.txt")
            self.save_to_file("./user_data")
            text("Sign-up successful. Your details have been saved.")
            random_color_star_print(23)
            sleep(1)
            return self.username
