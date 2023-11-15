# Write your solution here
limit = int(input("Limit?"))
power = 0
number = 2
while limit >= number ** power:
    print(number ** power)
    power += 1