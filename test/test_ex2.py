import math
import operator
import unittest

import ex2


class TestEx3(unittest.TestCase):
    def test_value(self):
        result = ex2.run_from_modules((math, operator), 'add', 1, 2.5)
        self.assertEqual(3.5, result)

    def test_type_checks(self):
        with self.assertRaises(TypeError):
            ex2.run_from_modules(3, 'add', 1, 2)
        with self.assertRaises(TypeError):
            ex2.run_from_modules((2, operator), 'add', 1, 2)
        with self.assertRaises(TypeError):
            ex2.run_from_modules((math, operator), 4.2, 1, 2)
        with self.assertRaises(TypeError):
            ex2.run_from_modules((math, operator), 'add', 'err')

    def test_unknown_function(self):
        with self.assertRaises(ValueError):
            ex2.run_from_modules((math, operator), 'do_code', 4, 2.0)

    def test_zero_division(self):
        # Provided by python modules.
        # We can't predict exact names of functions
        # that do division by the second argument.
        # Python modules can be modified and already do this check.
        with self.assertRaises(ZeroDivisionError):
            ex2.run_from_modules((math, operator), 'truediv', 1, 0)


if __name__ == '__main__':
    unittest.main()
