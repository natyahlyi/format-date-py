import click

from datetime import date
from itertools import permutations

# range of legal dates (default: between Jan 1, 2000 and Dec 31, 2999)
start_date, end_date = date(2000, 1, 1), date(2999, 12, 31)


@click.command()
@click.option('--file', type=click.Path(exists=True))
@click.option('--output', type=click.Path(exists=False))
@click.option('--interactive', is_flag=True)
def main(file, output, interactive):
    if interactive:
        date_format_i()
    elif file:
        with open(file, 'r') as f:
            input_lines = f.read().split('\n')
            date_format_f(input_lines, output)
    else:
        click.echo('Run interactive mode? [y/n]', nl=False)
        c = click.getchar()
        click.echo('\n')
        if c == 'y':
            date_format_i()
        elif c == 'n':
            click.echo('Abort!')
        else:
            click.echo('Invalid input :(')


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


def process(line):
    numbers = line.split('/')

    if len(numbers) != 3:
        raise ValueError

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
        desired_date = min(combinations)
    else:
        raise ValueError

    return desired_date


def date_format_f(input_lines, output):
    if output:
        with click.open_file(output, 'w+') as f:
            for line in input_lines:
                try:
                    desired_date = process(line)
                    f.write('{0} >> {1}'.format(line, desired_date) + '\n')
                except ValueError:
                    f.write('{0} >> Invalid input'.format(line) + '\n')

    else:
        for line in input_lines:
            console_output(line)


def date_format_i():
    while True:
        line = input("Date formatted A/B/C: ")
        console_output(line)


def console_output(line):
    try:
        desired_date = process(line)
        print('{0} >> {1}'.format(line, desired_date))
    except ValueError:
        print('{0} >> Invalid input'.format(line))


if __name__ == '__main__':
    main()