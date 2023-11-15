# Copy here code of line function from previous exercise
def line(x, y):
    if y != "":
        print(f"{x * y[0]}")
    else:
        print(x * "*")
def triangle(size):
    # You should call function line here with proper parameters
    height = 1
    while size >= height:
        line(height, "#")
        height += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
