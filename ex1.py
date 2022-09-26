import argparse
import operator


def calculate(a: float, action: str, b: float):
    actions = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    if action not in actions:
        raise AttributeError('Unsupported operator')

    func = actions[action]
    return func(a, b)


parser = argparse.ArgumentParser()
parser.add_argument('a', type=float)
parser.add_argument('action', type=str, choices=['+', '-', '*', '/'])
parser.add_argument('b', type=float)
args = parser.parse_args()

result = calculate(args.a, args.action, args.b)
print(result)
