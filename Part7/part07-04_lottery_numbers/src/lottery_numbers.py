# Write your solution here
from random import sample
def lottery_numbers(amount: int, lower: int, upper: int):
    lottery_numbers = []
    pool = list(range(lower, upper))
    sample_numbers = sample(pool, amount)
    sample_numbers = sorted(sample_numbers)
    for number in sample_numbers:
        lottery_numbers.append(number)
    return lottery_numbers
if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)