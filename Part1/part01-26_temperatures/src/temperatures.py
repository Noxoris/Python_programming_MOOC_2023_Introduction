# Write your solution here
fahrenheit = int(input("Fahrenheit?"))
celsius = (fahrenheit - 32) / 1.8
print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
    print("Brr! It's cold in here!")