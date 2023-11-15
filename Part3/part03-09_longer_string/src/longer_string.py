# Write your solution here
first_string = input("String?")
second_string = input("String 2?")
if len(first_string) > len(second_string):
    print(f" {first_string} is longer")
if len(first_string) < len(second_string):
    print(f" {second_string} is longer")
if len(first_string) == len(second_string):
    print(f"The strings are equally long")


