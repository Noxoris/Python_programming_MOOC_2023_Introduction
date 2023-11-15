# Write your solution here
def spruce(x):
    print("a spruce!")
    counter = 1
    y = x + 1
    z = 1
    while y > counter:
        print((x-1) * " " + z * "*")
        counter += 1
        x -= 1
        z += 2
    print((z//2 -1) * " " + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)