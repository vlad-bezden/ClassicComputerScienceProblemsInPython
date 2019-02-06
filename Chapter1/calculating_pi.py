"""pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 ..."""

import unittest
from itertools import cycle
import timeit


def calculate_pi_1(n_terms: int) -> float:
    return sum(4 / i * s for i, s in zip(range(1, n_terms, 2), cycle([1, -1])))


def calculate_pi_2(n_terms: int) -> float:
    return sum(4 / i for i in range(1, n_terms, 4)) - sum(
        4 / i for i in range(3, n_terms, 4)
    )


class Tests(unittest.TestCase):
    def test_1(self):
        result = calculate_pi_1(200)
        self.assertAlmostEqual(result, 3.14, 1)

    def test_2(self):
        result = calculate_pi_2(200)
        self.assertAlmostEqual(result, 3.14, 1)


if __name__ == "__main__":
    for f in [calculate_pi_1, calculate_pi_2]:
        t = timeit.timeit(stmt="f(1_000)", number=10, globals=globals())
        print(f"{f.__name__} took: {t:.6f}")
    unittest.main()
