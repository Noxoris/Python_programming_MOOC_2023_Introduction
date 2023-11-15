# Write your solution here
list = [] 
count = 0
while True:
    words = input("words?")
    if words in list:
        break
    list.append(words)
    count += 1
print(f"You typed in {count} different words")
    

