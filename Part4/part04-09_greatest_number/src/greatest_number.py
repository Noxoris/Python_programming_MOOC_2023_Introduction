# Write your solution here
def greatest_number(a,b,c):
    greatest = 0
    if a > b and a > c:
        greatest = a
        return a
    elif b > a and b > c:
        greatest = b
        return b
    elif c > a and c > a:
        greatest = c
        return c
    else:
        greatest = a
        return greatest
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)