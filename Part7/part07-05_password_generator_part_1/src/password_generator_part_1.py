# Write your solution here
import string
from random import choice
def generate_password(length):
    password = ""
    while len(password) < length:
       character = choice(string.ascii_lowercase)
       password += character
    return password
if __name__ == "__main__":
    for i in range(100):
        print(generate_password(18))