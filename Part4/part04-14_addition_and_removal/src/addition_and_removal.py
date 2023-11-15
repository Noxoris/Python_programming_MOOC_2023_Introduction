# Write your solution here
list = []
print("The list is now []")
while True:
    choice = input("a(d)d, (r)emove or e(x)it:")
    if choice == "d":
        list.append(len(list)+1)
        print(f"The list is now {list}")
    if choice == "r":
        list.pop(len(list)-1)
        print(f"The list is now {list}")   
    if choice == "x":
        break
print("Bye!")
    
        
