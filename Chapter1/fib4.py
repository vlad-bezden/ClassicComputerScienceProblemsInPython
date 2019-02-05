from functools import lru_cache
import unittest


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fib(1), 1)

    def test_2(self):
        self.assertEqual(fib(2), 1)

    def test_10(self):
        self.assertEqual(fib(50), 12_586_269_025)


if __name__ == "__main__":
    unittest.main(verbosity=2)
