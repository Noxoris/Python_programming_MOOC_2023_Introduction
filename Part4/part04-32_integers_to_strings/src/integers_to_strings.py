# Write your solution here
def formatted(list):
    new_list = []
    for i in list:
        i = f"{i:.2f}"
        new_list.append(i)
    return new_list

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)