# Write your solution here
def create_tuple(x: int, y: int, z: int):
    smallest = 0
    if x < y and x < z:
        smallest = x
    elif y < x and y < z:
        smallest = y
    elif z < x and z < y:
        smallest = z

    greatest = 0
    if x > y and x > z:
        greatest = x
    elif y > x and y > z:
        greatest = y
    elif z > x and z > y:
        greatest = z

    sum = x + y + z
    tuple = (smallest, greatest, sum)
    return tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))