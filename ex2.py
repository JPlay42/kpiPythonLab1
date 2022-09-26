import argparse
import math
import operator
from types import ModuleType


def check_tuple(arg: tuple, name: str, entry_type: type):
    if not all(isinstance(n, entry_type) for n in arg):
        raise AttributeError('Wrong entry type in ' + name)


def run_from_modules(modules: tuple, func_name: str, *params: tuple):
    check_tuple(modules, 'modules', ModuleType)

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
