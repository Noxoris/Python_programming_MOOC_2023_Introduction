# Write your solution here
sent = input("Please type in a sentence:")
number = 0
if len(sent) != 0:
    print(sent[0])
    while number < len(sent):
        if sent[number] == " ":
            print(sent[number+1])
        number += 1