# Write your solution here
limit = int(input("Limit?"))
number = int(input("Base?"))
power = 0
while limit >= number ** power:
    print(number ** power)
    power += 1