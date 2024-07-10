import os
from time import sleep
import random
import pyfiglet
import platform
from colorama import init, Fore, Style

# Check if the platform is Windows
is_windows = platform.system() == "Windows"

# Initialize colorama
init()

# ANSI color codes
color_codes = [
    Fore.RED,      # Red
    Fore.GREEN,    # Green
    Fore.YELLOW,   # Yellow
    Fore.MAGENTA,  # Purple
    Fore.CYAN,     # Cyan
    Fore.WHITE,    # White
    Fore.LIGHTRED_EX,    # Light Red
    Fore.LIGHTGREEN_EX,  # Light Green
    Fore.LIGHTYELLOW_EX, # Light Yellow
    Fore.LIGHTBLUE_EX,   # Light Blue
    Fore.LIGHTMAGENTA_EX,# Light Purple
    Fore.LIGHTCYAN_EX,   # Light Cyan
    Fore.LIGHTWHITE_EX
]

# Reset color code
reset_code = Style.RESET_ALL

# Function to print text with a specific color and delay
def print_with_color(message, color_code, end='\n', delay=0.003):
    for char in message:
        print(f"{color_code}{char}", end='', flush=True)
        sleep(delay)
    print(reset_code, end=end)

# Function to print random color text with delay
def text(message, end='\n', delay=0.003):
    color_code = random.choice(color_codes)
    print_with_color(message, color_code, end, delay)

# Function to print large ASCII art text
def print_large_text(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)
def welcome():
    pass

# Function to print star pattern in random colors
def star_print(message, n):
    stars = '<>'
    for _ in range(n):
        color_code = random.choice(color_codes)
        print_with_color(stars, color_code, end='')
    print()
    text(f'{message}'.center(n * 2))
    for _ in range(n):
        color_code = random.choice(color_codes)
        print_with_color(stars, color_code, end='')
    print()

def random_color_star_print(n, delay=0.003):
    stars = '<>' * n
    for char in stars:
        color_code = random.choice(color_codes)
        print_with_color(char, color_code, end='', delay=delay)
    print(reset_code)

def clear_screen():
    if is_windows:
        os.system('cls')
    else:
        os.system('clear')
