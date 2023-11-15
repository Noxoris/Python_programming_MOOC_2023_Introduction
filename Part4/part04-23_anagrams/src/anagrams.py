# Write your solution here
def anagrams(first_word : str, second_word: str):
    if sorted(first_word) == sorted(second_word):
        return True
    else:
        return False
if __name__ == "__main__":
    print(anagrams("tame", "meta")) 
    print(anagrams("tame", "mate")) 
    print(anagrams("tame", "team")) 
    print(anagrams("tabby", "batty")) 
    print(anagrams("python", "java")) 