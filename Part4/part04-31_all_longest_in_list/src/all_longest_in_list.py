# Write your solution here
def all_the_longest(list):
    new_list = []
    longest = len(list[0])
    for i in list:
        if len(i) >= longest:
            longest = len(i)
    for i in list:
        if len(i) == longest:
            new_list.append(i)
    return new_list

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)