# Copy here code of line function from previous exercise and use it in your solution
def line(x, y):
    if y != "":
        print(f"{x * y[0]}")
    else:
        print(x * "*")
def shape (count,character,rect_h,filler):
    height = 1
    while count >= height:
        line(height, character)
        height += 1
    limit = rect_h
    while limit > 0:
        line(count, filler)
        limit -= 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")