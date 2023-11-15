# Write your solution here
def oldest_person(people: list):
    oldest = people[0][1]
    for person in people:
        year = person[1]
        if oldest < year:
            oldest = year
    return oldest
def oldest_person(people: list):
    name_oldest = people[0][0]
    age_oldest = people[0][1]
    for i in people:
        if i[1] < age_oldest:
            age_oldest = i[1]
            name_oldest = i[0]
    return name_oldest

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))  

   