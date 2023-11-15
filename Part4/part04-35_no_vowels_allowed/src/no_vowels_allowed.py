# Write your solution here
def no_vowels(word):
    for letter in 'aeiou':
        word = word.replace(letter, '')
    return word
if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))