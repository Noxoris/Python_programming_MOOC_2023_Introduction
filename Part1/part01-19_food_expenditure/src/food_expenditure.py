# Write your solution here
cafe = int(input("Cafe?"))
price = float(input("Price?"))
groceries = float(input("Groceries?"))
weekly = cafe * price + groceries
daily = weekly / 7
print (f"Average food expenditure: Daily: {weekly/7} euros \n Weekly: {weekly} euros")