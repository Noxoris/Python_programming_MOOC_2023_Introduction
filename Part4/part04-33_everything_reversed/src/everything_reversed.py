# Write your solution here
def everything_reversed(list):
    new_list = []
    i = len(list) - 1
    while i >= 0:
        reverse = list[i]
        new_list.append(reverse[::-1])
        i -= 1
    return new_list
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)