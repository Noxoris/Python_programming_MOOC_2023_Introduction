# write your solution here
text = input("Text?")
list = text.split(' ')
list_of_words = []
with open ("wordlist.txt") as dictionary:
    for line in dictionary:
        line = line.replace('\n', '')
        parts = line.split(',')
        list_of_words.append(line)
    new = " "
    for word in list:
            if word.lower() in list_of_words:
                new += word
            else:
                new += "*" + word + "*" 
            new += " "
    print(new)

    
    