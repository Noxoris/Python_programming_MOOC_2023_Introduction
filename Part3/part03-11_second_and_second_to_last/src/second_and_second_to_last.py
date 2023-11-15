# Write your solution here
word = input("String?")
length = len(word)
second = word[1]
second_to_last = word[length - 2]
if second_to_last == second:
    print(f"The second and the second to last characters are {second}")
else:
    print("The second and the second to last characters are different")
    