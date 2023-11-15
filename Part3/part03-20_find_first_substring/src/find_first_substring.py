# Write your solution here
word = input("Word?")
char = input("char?")
search = word.find(char)
char_end = search + 3
result = len(word[search:char_end])
if result >= 3:
    print(word[search:char_end])
