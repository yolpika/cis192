import unittest
from hw1 import *

""" You can use this file as follows:
1. Make sure test1.py is in the same folder as hw1.py.
2. run `python3 test1.py` -> this should show `OK` if your tests all pass,
   or some failure messages if not.
3. Write more test cases to ensure your code is correct!
"""

class TestHomework1(unittest.TestCase):

    def setUp(self):
        pass

    # fizzbuzz
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')

    # snapcrackle
    def test_snapcrackle(self):
        self.assertEqual(snapcrackle(3), 'Snap')

    # is_prime
    def test_is_prime(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_2(self):
        self.assertTrue(is_prime(2))

    # nth_prime
    def test_nth_prime(self):
        self.assertEqual(nth_prime(5), 11)

    # gcd iter
    def test_gcd_iter(self):
        self.assertEqual(gcd_iter(10, 1), 1)

    # gcd rec
    def test_gcd_rec(self):
        self.assertEqual(gcd_rec(10, 1), 1)

    # fib iter
    def test_fib_iter(self):
        self.assertEqual(fib_iter(8), 13)

    # fib rec
    def test_fib_rec(self):
        self.assertEqual(fib_rec(8), 13)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
