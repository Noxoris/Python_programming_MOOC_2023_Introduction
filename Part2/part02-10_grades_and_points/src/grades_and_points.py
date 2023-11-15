# Write your solution here
pt = int(input("Points?"))
if pt < 0:
    print("impossible!")
elif pt >= 0 and pt < 49 :
    print("fail")
elif pt >= 50 and pt <= 59 :
    print("Grade: 1")
elif pt >= 60 and pt <= 69 :
    print("Grade: 2")
elif pt >= 70 and pt <= 79 :
    print("Grade: 3")
elif pt >= 80 and pt <= 89 :
    print("Grade: 4")
elif pt >= 90 and pt <= 100 :
    print("Grade: 5")
elif pt > 100:
    print("impossible!")