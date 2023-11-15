# Write your solution here
from string import ascii_letters, punctuation
def separate_characters(my_string: str):
    ascii = ''
    punctuation_char = ''
    other = ''
    for letter in my_string:
        if letter in ascii_letters:
            ascii += letter
        elif letter in punctuation:
            punctuation_char += letter
        else:
            other += letter
    return(ascii, punctuation_char, other)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])


