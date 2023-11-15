# Write your solution here
word = input("Input?")
length = len(word)
part = 1
while length > 0:
    print(word[:part])
    part += 1
    length -= 1