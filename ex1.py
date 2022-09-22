import argparse


def calculate(a: float, action, b: float):
    match action:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
    return ValueError('Unsupported action')


parser = argparse.ArgumentParser()
parser.add_argument('a', type=float)
parser.add_argument('action', type=str, choices=['+', '-', '*', '/'])
parser.add_argument('b', type=float)
args = parser.parse_args()

result = calculate(args.a, args.action, args.b)
print(result)
