"""
Three vertical pegs (henceforth “towers”) stand tall.
We will label them A, B, and C. Donutshaped discs are around tower A.
The widest disc is at the bottom, and we will call it disc 1.
The rest of the discs above disc 1 are labeled with increasing numerals
and get progressively narrower. For instance, if we were to work with three discs,
the widest disc, the one on the bottom, would be 1.
The next widest disc, disc 2, would sit on top of disc 1.
And finally, the narrowest disc, disc 3, would sit on top of disc 2.
Our goal is to move all of the discs from tower A to tower C given the
following constraints:
• Only one disc can be moved at a time.
• The topmost disc of any tower is the only one available for moving.
• A wider disc can never be atop a narrower disc.
"""

from queue import LifoQueue
import unittest

NUMBER_OF_DISCS = 3


def hanoi(
    from_peg: LifoQueue, to_peg: LifoQueue, other_peg: LifoQueue, disk: int
) -> None:
    """
    Move the top n disks from peg from_peg to peg to_peg
    using other_peg to hold disks temporarily as needed.
    """
    # buttom one
    if disk == 1:
        to_peg.put(from_peg.get())
    else:
        # recursively move the top n - 1 disks from from_peg to other_peg
        hanoi(from_peg, other_peg, to_peg, disk - 1)
        # move the last disk from from_peg to to_peg
        hanoi(from_peg, to_peg, other_peg, 1)
        # recursively move the top n - 1 disks back from other_peg to to_peg
        hanoi(other_peg, to_peg, from_peg, disk - 1)


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
