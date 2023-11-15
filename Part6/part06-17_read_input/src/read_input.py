# Write your solution here
def read_input(text, x, y):
    while True:
        number = input(text)     
        try:
            int_number = int(number)
            if int_number >= x and int_number <= y:
                return int_number
            else:
                print(f"You must type in an integer between {x} and {y}")
        except ValueError:
            print(f"You must type in an integer between {x} and {y}")
