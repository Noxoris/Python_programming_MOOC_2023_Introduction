# Write your solution here
tries = 0
password = 4321
while True:
    pin = int(input("PIN"))
    tries += 1
    if pin == password and tries > 1:
        print(f"Correct! It took you {tries} attempts")
        break
    elif pin != password:
        print("Wrong")
    elif pin == password and tries == 1:
        print(f"Correct! It only took you one single attempt!")
        break


