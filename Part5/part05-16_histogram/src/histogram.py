# Write your solution here
def histogram(word : str):
    letter_list = {}
    for letter in word:
        if letter not in letter_list:
            letter_list[letter] = 0
        letter_list[letter] += 1
    for key, value in letter_list.items():
        print(key + " " +  value *"*")
   
if __name__ == "__main__":
    histogram("statistically")
    