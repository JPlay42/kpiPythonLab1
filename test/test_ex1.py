import unittest

import ex1


class TestEx1(unittest.TestCase):
    def test_value(self):
        self.assertEqual(3.0, ex1.calculate(1, '+', 2.0))

    def test_type_checks(self):
        with self.assertRaises(TypeError):
            ex1.calculate('duck', '+', 2)
        with self.assertRaises(TypeError):
            ex1.calculate(1, '+', 'cock')
        with self.assertRaises(TypeError):
            ex1.calculate(1, 2, 3)

    def test_unknown_operation(self):
        with self.assertRaises(ValueError):
            ex1.calculate(1, '=', 3)

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            ex1.calculate(3, '/', 0)


if __name__ == '__main__':
    unittest.main()
