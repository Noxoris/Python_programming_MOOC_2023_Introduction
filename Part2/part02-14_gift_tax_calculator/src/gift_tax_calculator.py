# Write your solution here
gift = float(input("Gift?"))
if gift == 5000:
    print("Amount of tax: 100.0 euros")
elif gift > 5000 and 25000 > gift :
    tax = 100 + ((gift - 5000)*0.08)
    print(f"Amount of tax: {tax} euros")
elif gift >= 25000 and 55000 > gift :
    tax = 1700 + ((gift - 25000)*0.1)
    print(f"Amount of tax: {tax} euros")
elif gift >= 55000 and 200000 > gift :
    tax = 4700 + ((gift - 55000)*0.12)
    print(f"Amount of tax: {tax} euros")
elif gift >= 200000 and 1000000 > gift :
    tax = 22100 + ((gift - 200000)*0.15)
    print(f"Amount of tax: {tax} euros")
elif gift >= 1000000:
    tax = 142100 + ((gift - 1000000)*0.17)
    print(f"Amount of tax: {tax} euros")
else:
    print("No tax!")
