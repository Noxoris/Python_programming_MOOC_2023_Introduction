# Write your solution here
def dict_of_numbers():
    new_dictionary = {}
    all = []
    zero = ['zero']
    word_first = ['one', 'two', 'three','four', 'five', 'six','seven', 'eight', 'nine']
    word_teen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    word_ten = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    rest = []
    for i in range(100):
        all.append(i)

    for first in range(len(word_ten)):
        rest.append(word_ten[first])
        for second in range(len(word_first)):
            rest.append(word_ten[first] + "-" + word_first[second])
    list = []
    list.append(zero[0])
    for i in word_first:
        list.append(i)
    for i in word_teen:
        list.append(i)
    for i in rest:
        list.append(i)
    new_dictionary = {all[i] : list[i] for i in range(len(all))}
    return new_dictionary


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
