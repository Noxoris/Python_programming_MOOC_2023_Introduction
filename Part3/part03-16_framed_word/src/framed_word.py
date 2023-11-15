# Write your solution here
word = input("Please type in a string: ")
length = len(word)
if length % 2 != 0:
    print(30 * "*")
    print("*" + ((30 - length)//2)  * " " + word + ((30 - length)//2 - 1) * " " + "*" )
    print(30 * "*")
else :
    print(30 * "*")
    print("*" + ((30 - length)//2 -1)  * " " + word + ((30 - length)//2 -1) * " " + "*" )
    print(30 * "*")
