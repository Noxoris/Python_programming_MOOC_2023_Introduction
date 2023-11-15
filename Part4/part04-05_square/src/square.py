# Copy here code of line function from previous exercise
def line(x, y):
    if y != "":
        print(f"{x * y[0]}")
    else:
        print(x * "*")
def square(size, character):
    # You should call function line here with proper parameters
    timer = size
    while timer > 0:
        line(size, character)
        timer -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")