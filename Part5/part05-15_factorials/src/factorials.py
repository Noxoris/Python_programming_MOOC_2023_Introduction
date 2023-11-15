# Write your solution here
def factorials(n: int):
    new_dictionary = {}
    result = 1
    for i in range(1, n+1):
        result *= i
        new_dictionary[i] = result
    return new_dictionary

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])