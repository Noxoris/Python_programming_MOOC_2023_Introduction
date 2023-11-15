# write your solution here
names = {}
student_file = input("Student information: ")
exercise_file = input("exercises completed: ")
with open(student_file) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';') 
        if parts[0] == "id": 
            continue 
        names[parts[0]] = parts[1:3]

exercises = {} 
 
with open(exercise_file) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        for exercise in parts[1:]:
            exercises[parts[0]] = (parts[1:])


for id, name in names.items():
    if id in exercises:
        exercise = exercises[id]
        print(f"{name} {exercise}")