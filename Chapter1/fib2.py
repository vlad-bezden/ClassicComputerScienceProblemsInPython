import unittest


def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fib(1), 1)

    def test_2(self):
        self.assertEqual(fib(2), 1)

    def test_10(self):
        self.assertEqual(fib(10), 55)


if __name__ == "__main__":
    unittest.main()
