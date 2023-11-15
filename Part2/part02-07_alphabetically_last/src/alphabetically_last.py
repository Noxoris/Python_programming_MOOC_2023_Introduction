# Write your solution here
first_word = input("Word1?")
second_word = input("Word2?")
if first_word > second_word:
    print(f"{first_word} comes alphabetically last.")
elif first_word < second_word:
    print(f"{second_word} comes alphabetically last.")
else:
    print("You gave the same word twice.")