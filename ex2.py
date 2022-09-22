import argparse
import math
import operator


def run_from_modules(modules, func_name, *params):
    for module in modules:
        if hasattr(module, func_name):
            func = getattr(module, func_name)
            return func(*params)

    raise AttributeError('Function \'' + func_name + "\' is not found")


parser = argparse.ArgumentParser()
parser.add_argument('func', type=str)
parser.add_argument('params', type=float, nargs='+')
args = parser.parse_args()

print(run_from_modules((math, operator), args.func, *args.params))
