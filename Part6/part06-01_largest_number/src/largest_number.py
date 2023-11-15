# write your solution here
def  largest():
    with open("numbers.txt") as new_file:
        numbers = []
        for line in new_file: 
            numbers.append(int(line))
        numbers_sorted = sorted(numbers)
        return numbers_sorted[len(numbers_sorted) - 1]

if __name__ == "__main__":
    largest()