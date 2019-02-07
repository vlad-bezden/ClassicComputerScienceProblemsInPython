import unittest
from typing import TypeVar, Iterable, Sequence


T = TypeVar("T")


def linear_contains(iterable: Iterable[T], key: T) -> bool:
    return any(item == key for item in iterable)


def binary_contains(sequence: Sequence[T], key: T) -> bool:
    low = 0
    high = len(sequence) - 1

    while low <= high:
        mid = (high + low) // 2
        if key < sequence[mid]:
            high = mid - 1
        elif sequence[mid] < key:
            low = mid + 1
        else:
            return True
    return False


class Test(unittest.TestCase):
    def test_linear_contains_exist(self):
        data = [1, 5, 15, 15, 15, 15, 20]
        self.assertTrue(linear_contains(data, 5))

    def test_binary_contains_exist(self):
        data = list("adefz")
        self.assertTrue(binary_contains(data, "f"))

    def test_binary_contains_dont_exist(self):
        data = ["john", "mark", "ronald", "sarah"]
        self.assertFalse(binary_contains(data, "sheila"))


if __name__ == "__main__":
    unittest.main()
