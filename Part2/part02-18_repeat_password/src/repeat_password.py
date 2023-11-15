# Write your solution here
password = input("Pass?")
while True:
    password_check = input("Repeat?")
    if password != password_check:
        print("They do not match!")
    else:
        print("User account created!")
        break