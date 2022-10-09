import unittest

import ex3


class TestEx3(unittest.TestCase):
    def test_value(self):
        result = ex3.ebnf('1-7+28-5-1+16')
        self.assertEqual(32, result)

    def test_type_check(self):
        with self.assertRaises(TypeError):
            ex3.ebnf(42)

    def test_unsupported_operator(self):
        with self.assertRaises(ValueError):
            ex3.ebnf('2*2')

    def test_characters_sequence(self):
        with self.assertRaises(ValueError):
            ex3.ebnf('+1+1')
        with self.assertRaises(ValueError):
            ex3.ebnf('1+1+')
        with self.assertRaises(ValueError):
            ex3.ebnf('1++1')
        ex3.ebnf('1+1+1')


if __name__ == '__main__':
    unittest.main()
