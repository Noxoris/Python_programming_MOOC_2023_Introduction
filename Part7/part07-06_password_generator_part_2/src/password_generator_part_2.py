# Write your solution here
import string
from random import choice
def generate_strong_password(length, arg1, arg2):
    special = "!?=+-()#"
    char_all = string.ascii_lowercase + special + string.digits
    char_letter_number = string.ascii_lowercase + string.digits
    password = ""
    if arg1 and arg2:
        while len(password) < length:
            character = choice(char_all)
            password += character
        
    elif arg1:
        while len(password) < length:
            character = choice(char_letter_number) 
            password += character

    elif arg2:
        while len(password) < length:
            character = choice(string.ascii_lowercase + special)
            password += character
    else:
        while len(password) < length:
            character = choice(string.ascii_lowercase)
            password += character
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(5, True, False))