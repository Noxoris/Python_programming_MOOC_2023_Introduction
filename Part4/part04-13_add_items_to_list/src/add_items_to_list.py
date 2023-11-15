# Write your solution here
items = int(input("Items?"))
list = []
while items > 0:
    list.append(int(input("Value?")))
    items -= 1
print(list)