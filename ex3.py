import argparse


def add_number(num_buf: str, num_list: list):

    if num_buf == '':
        # sign after sign, like '2++2'
        # or sign at the beginning, like '+2+3'
        raise AttributeError('Operation sign must be after the number')

    num_list.append(int(num_buf))


def calculate(numbers: list, signs: list):
    if not isinstance(numbers, list) or not all(isinstance(n, int) for n in numbers):
        raise AttributeError('Wrong type of \'numbers\'')

    if not isinstance(signs, list) or not all(isinstance(n, bool) for n in signs):
        raise AttributeError('Wrong type of \'signs\'')

    result = numbers[0]
    for i in range(0, len(signs)):
        if signs[i]:  # if it's equal to '+'
            result += numbers[i + 1]
        else:
            result -= numbers[i + 1]

    return result


def ebnf(input_string):
    numbers = []
    signs = []

    number_buf = ''
    for char in input_string:
        if char.isdigit():
            number_buf += char
        elif char in ('+', '-'):
            add_number(number_buf, numbers)
            number_buf = ''
            signs.append(char == '+')  # memory optimization, we store bool instead of str
        else:
            raise ValueError('Unsupported character')

    add_number(number_buf, numbers)

    if len(numbers) - len(signs) != 1:
        raise ValueError('Invalid format')

    return calculate(numbers, signs)


parser = argparse.ArgumentParser()
parser.add_argument('expression', type=str)
args = parser.parse_args()
input_str = args.expression

try:
    print("True, " + str(ebnf(input_str)))
except ValueError:
    print("False, None")
