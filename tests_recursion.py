import unittest
from recursion import (
    sum_series,
    sum_while,
    sum_recursive,
    factorial_while,
    factorial_recursive,
    fibonacci_iterative,
    fibonacci_iterative_optimized,
    fibonacci_recursive
)

class TestRecursion(unittest.TestCase):
    def test_sum_series(self):
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(3), 6)
        self.assertEqual(sum_series(5), 15)
        self.assertEqual(sum_series(10), 55)

    def test_sum_while(self):
        self.assertEqual(sum_while(0), 0)
        self.assertEqual(sum_while(1), 1)
        self.assertEqual(sum_while(3), 6)
        self.assertEqual(sum_while(5), 15)
        self.assertEqual(sum_while(10), 55)

    def test_sum_recursive(self):
        self.assertEqual(sum_recursive(0), 0)
        self.assertEqual(sum_recursive(1), 1)
        self.assertEqual(sum_recursive(3), 6)
        self.assertEqual(sum_recursive(5), 15)
        self.assertEqual(sum_recursive(10), 55)

    def test_factorial_while(self):
        self.assertEqual(factorial_while(0), 1)
        self.assertEqual(factorial_while(1), 1)
        self.assertEqual(factorial_while(3), 6)
        self.assertEqual(factorial_while(5), 120)
        self.assertEqual(factorial_while(6), 720)

    def test_factorial_recursive(self):
        self.assertEqual(factorial_recursive(0), 1)
        self.assertEqual(factorial_recursive(1), 1)
        self.assertEqual(factorial_recursive(3), 6)
        self.assertEqual(factorial_recursive(5), 120)
        self.assertEqual(factorial_recursive(6), 720)

    def test_fibonacci_iterative(self):
        self.assertEqual(fibonacci_iterative(0), 0)
        self.assertEqual(fibonacci_iterative(1), 1)
        self.assertEqual(fibonacci_iterative(3), 2)
        self.assertEqual(fibonacci_iterative(5), 5)
        self.assertEqual(fibonacci_iterative(10), 55)

    def test_fibonacci_iterative_optimized(self):
        self.assertEqual(fibonacci_iterative_optimized(0), 0)
        self.assertEqual(fibonacci_iterative_optimized(1), 1)
        self.assertEqual(fibonacci_iterative_optimized(3), 2)
        self.assertEqual(fibonacci_iterative_optimized(5), 5)
        self.assertEqual(fibonacci_iterative_optimized(10), 55)

    def test_fibonacci_recursive(self):
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci_recursive(3), 2)
        self.assertEqual(fibonacci_recursive(5), 5)
        self.assertEqual(fibonacci_recursive(10), 55)

unittest.main()