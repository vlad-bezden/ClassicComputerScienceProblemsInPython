"""
Three vertical pegs (henceforth “towers”) stand tall.
We will label them A, B, and C. Donutshaped discs are around tower A.
The widest disc is at the bottom, and we will call it disc 1.
The rest of the discs above disc 1 are labeled with increasing numerals
and get progressively narrower. For instance, if we were to work with three discs,
the widest disc, the one on the bottom, would be

1. The next widest disc, disc 2, would sit on top of disc 1. And finally,
the narrowest disc, disc 3, would sit on top of disc 2.
Our goal is to move all of the discs from tower A to tower C given the
following constraints:
• Only one disc can be moved at a time.
• The topmost disc of any tower is the only one available for moving.
• A wider disc can never be atop a narrower disc.
"""

from queue import LifoQueue
import unittest

NUMBER_OF_DISCS = 20


def hanoi(begin: LifoQueue, end: LifoQueue, temp: LifoQueue, disk: int) -> None:
    # buttom one
    if disk == 1:
        end.put(begin.get())
    else:
        hanoi(begin, temp, end, disk - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, disk - 1)


class Test(unittest.TestCase):
    def test(self):
        tower_a = LifoQueue(NUMBER_OF_DISCS)
        tower_b = LifoQueue(NUMBER_OF_DISCS)
        tower_c = LifoQueue(NUMBER_OF_DISCS)

        for i in range(1, NUMBER_OF_DISCS + 1):
            tower_a.put(i)
        print("A:", tower_a.queue)
        self.assertTrue(tower_a.full())
        self.assertTrue(tower_b.empty())
        self.assertTrue(tower_c.empty())

        hanoi(tower_a, tower_c, tower_b, NUMBER_OF_DISCS)

        print("A:", tower_a.queue)
        print("B:", tower_b.queue)
        print("C:", tower_c.queue)

        self.assertTrue(tower_a.empty())
        self.assertTrue(tower_b.empty())
        self.assertTrue(tower_c.full())
        self.assertListEqual(tower_c.queue, list(range(1, NUMBER_OF_DISCS + 1)))


if __name__ == "__main__":
    unittest.main()
