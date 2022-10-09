import unittest

import ex4


class MyTestCase(unittest.TestCase):
    def test_type_check(self):
        with self.assertRaises(TypeError):
            ex4.knapsack('elephant', [3, 4, 5])
        with self.assertRaises(TypeError):
            ex4.knapsack(56, 'dog')
        with self.assertRaises(TypeError):
            ex4.knapsack(56, [1, 2, 'what?'])

    def test_value(self):
        self.assertEqual(18, ex4.knapsack(56, [3, 4, 5, 6]))
        self.assertEqual(43, ex4.knapsack(44, [17, 24, 19]))


if __name__ == '__main__':
    unittest.main()
