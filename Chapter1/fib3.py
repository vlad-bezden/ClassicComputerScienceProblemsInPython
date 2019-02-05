import unittest
from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}


def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fib(1), 1)

    def test_2(self):
        self.assertEqual(fib(2), 1)

    def test_10(self):
        self.assertEqual(fib(50), 12_586_269_025)


if __name__ == "__main__":
    unittest.main(verbosity=2)
