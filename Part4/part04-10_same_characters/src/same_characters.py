# Write your solution here
def same_chars(word,number,number_two):      
    if number > len(word) - 1 or number_two > len(word) - 1 or word[number] != word[number_two]:
         return False
    if word[number] == word[number_two]:
           return True
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 1, 3))