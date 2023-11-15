# Write your solution here
def times_ten(start_index: int, end_index: int):
    new_dictionary = {}
    i = start_index 
    while i <= end_index:
        new_dictionary[start_index] = start_index * 10
        i += 1
        start_index += 1
    return new_dictionary

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)