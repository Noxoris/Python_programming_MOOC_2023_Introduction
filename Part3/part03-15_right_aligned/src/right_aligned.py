# Write your solution here
word = input("Please type in a string: ")
length = len(word)
if length != 20:
    print((20 - length) * "*" + word)
   