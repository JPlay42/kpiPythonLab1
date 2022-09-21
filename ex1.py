import argparse


def calculate(a, action, b):
    match action:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b


parser = argparse.ArgumentParser()
parser.add_argument('a', type=float)
parser.add_argument('action', type=str, choices=['+', '-', '*', '/'])
parser.add_argument('b', type=float)
args = parser.parse_args()

result = calculate(args.a, args.action, args.b)
print(result)
