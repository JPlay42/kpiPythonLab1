import argparse
import operator


def calculate(a: float | int, action: str, b: float | int):
    if not isinstance(a, float | int):
        raise TypeError('A is neither float nor int')

    if not isinstance(b, float | int):
        raise TypeError('B is neither float nor int')

    actions = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    if not isinstance(action, str):
        raise TypeError('Action is not string')

    if action not in actions:
        raise ValueError('Unsupported operator')

    if action == '/' and b == 0:
        raise ValueError('Division by zero')

    func = actions[action]
    return func(a, b)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('a', type=float)
    parser.add_argument('action', type=str, choices=['+', '-', '*', '/'])
    parser.add_argument('b', type=float)
    args = parser.parse_args()

    result = calculate(args.a, args.action, args.b)
    print(result)
