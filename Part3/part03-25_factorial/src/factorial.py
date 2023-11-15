# Write your solution here
base = 1
while True:
    number = int(input("Number?"))
    if number <= 0:
        break
    limit = 1
    while limit <= number:
        base *= limit
        limit += 1
    print(f"The factorial of the number {number} is {base}")
    base = 1
print("Thanks and bye!")