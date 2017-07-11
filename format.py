from datetime import date
from itertools import permutations

# range of legal dates (default: between Jan 1, 2000 and Dec 31, 2999)
start_date, end_date = date(2000, 1, 1), date(2999, 12, 31)


# TODO: Should not return None
def datify(x):
    d, m, y = x
    if d == m == '0' or m == y == '0':
        return None

    if len(y) < 2:
        y = '200' + y
    elif len(y) < 3:
        y = '20' + y
    elif len(y) < 4:
        y = '2' + y

    try:
        return date(int(y), int(m), int(d))
    except ValueError:
        return None

# TODO: implement "click"
if __name__ == '__main__':
    with open("data.txt", 'r') as file:
        input_lines = file.read().split('\n')

    for line in input_lines:
        numbers = line.split('/')

        # print(numbers)

        if len(numbers) != 3:
            print('{0} >> Invalid input'.format(line))
            continue

        # create six combinations of the same list with items in different order
        combinations = [x for x in permutations(numbers, 3)]

        # remove duplicates
        combinations = list(set(combinations))
        # converting sets of numbers to datetime objects
        combinations = [datify(x) for x in combinations]
        # removing rubbish
        combinations = list(filter(None, combinations))
        # checking if date is in the defined period of time
        combinations = list(filter(lambda x: start_date <= x <= end_date, combinations))
        if combinations:
            # selecting the earliest possible legal date
            combinations = min(combinations)
        else:
            print('{0} >> Invalid input'.format(line))
            continue

        print('{0} >> {1}'.format(line, combinations))
