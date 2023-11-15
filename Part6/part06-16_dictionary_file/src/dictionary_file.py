# Write your solution here
def adding_to_dict(en_word, fin_word):
    with open("dictionary.txt","a") as dict:
        dict.write(en_word + ";" + fin_word +"\n")
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    number = int(input("Function: "))
    if number == 1:
        fin = input("The word in Fin1nish: ")
        en = input("The word in English: ")
        adding_to_dict(fin, en)
        print("Dictionary entry added")
    elif number == 2:
        search_term = input("Search term: ")
        search_term = search_term.lower()
        with open("dictionary.txt") as dict:
            for line in dict:
                line = line.replace('\n', '')
                line = line.strip()
                parts = line.split(";")
                fin_part = parts[0].lower()
                en_part = parts[1].lower()
                if search_term in fin_part or search_term in en_part:
                        print(f"{fin_part} - {en_part}")
                        

    elif number == 3:
        print("Bye!")
        print()
        break
