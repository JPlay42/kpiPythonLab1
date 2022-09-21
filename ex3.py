import argparse


def add_number(num_buf, num_list):
    if num_buf == '':
        # sign after sign, like '2++2'
        # or sign at the beginning, like '+2+3'
        raise ValueError('Operation sign must be after the number')
    num_list.append(int(num_buf))


def calculate(numbers, signs):
    result = numbers[0]
    for i in range(0, len(signs)):
        if signs[i] == '+':
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
            signs.append(char)
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
