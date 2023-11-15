# Write your solution here
word = input("String?")
length = len(word)
back = length - (length + 1)
while back < 0 and back >= length * (-1):
    print(word[back])
    back -= 1
    
