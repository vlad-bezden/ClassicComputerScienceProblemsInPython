"""Keep it simple, Fibonacci"""

import unittest


def fib(n: int) -> int:
    if n == 0:
        return n
    a: int = 0
    b: int = 1

    for _ in range(1, n):
        a, b = b, a + b
    return b


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fib(1), 1)

    def test_2(self):
        self.assertEqual(fib(2), 1)

    def test_10(self):
        self.assertEqual(fib(50), 12_586_269_025)


if __name__ == "__main__":
    unittest.main(verbosity=2)
