# Write your solution here
students = int(input("Students?"))
groups = int(input("Size?"))
group_number = students // groups
students_left = students % groups
if students_left > 0:
  group_number = group_number + 1
print(f"Number of groups formed: {group_number}")