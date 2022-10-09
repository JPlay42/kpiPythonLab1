import argparse
import math
import operator
from types import ModuleType


def run_from_modules(modules: tuple, func_name: str, *params: int | float):
    if not isinstance(func_name, str):
        raise TypeError('Function name is not a string')

    if not isinstance(modules, tuple):
        raise TypeError('Modules is not a tuple')

    if not isinstance(params, tuple):
        raise TypeError('Params is not a tuple')

    if not all(isinstance(param, float | int) for param in params):
        raise TypeError('Params should be either int or float')

    for module in modules:
        if not isinstance(module, ModuleType):
            raise TypeError('Modules tuple should contain only modules')

        if hasattr(module, func_name):
            func = getattr(module, func_name)
            return func(*params)

    raise ValueError('Function \'' + func_name + "\' is not found")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('func', type=str)
    parser.add_argument('params', type=float, nargs='+')
    args = parser.parse_args()
    print(run_from_modules((math, operator), args.func, *args.params))
