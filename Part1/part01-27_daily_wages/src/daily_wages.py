# Write your solution here
wage = float(input("Wage?"))
hours = int(input("Hours?"))
week_day = input("Day?")
if week_day == "Sunday":
    wage = wage * 2
daily_wage = wage * hours
print(f"Daily wages: {daily_wage} euros")