"""Generating Fibonacci numbers with a generator"""

import unittest
from typing import Iterator


def fib(n: int) -> Iterator[int]:
    if n == 0:
        yield n
    a: int = 0
    b: int = 1

    for _ in range(1, n):
        a, b = b, a + b
    yield b


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(next(fib(1)), 1)

    def test_2(self):
        self.assertEqual(next(fib(2)), 1)

    def test_10(self):
        self.assertEqual(next(fib(50)), 12_586_269_025)


if __name__ == "__main__":
    unittest.main(verbosity=2)
