# Write your solution here
year = int(input("Give year:"))
year += 1
original = year
leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 ==0

while not leap:
    year += 1
    leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 ==0

print(f"The next leap year after {original-1} is {year}")
            
        






