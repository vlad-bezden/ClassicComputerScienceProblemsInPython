from enum import IntEnum
from typing import List
import unittest
from collections import namedtuple


Nucleotide = IntEnum("Nucleotide", ("A", "C", "G", "T"))
Codon = namedtuple("Codon", ["N1", "N2", "N3"])
Gene = List[Codon]

GENE_STR = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def str_to_gene(s: str) -> Gene:
    iters = [iter(s)] * 3
    return [Codon(a, b, c) for a, b, c in zip(*iters)]


def linear_contains(gene: Gene, codon: Codon) -> bool:
    return any(g == codon for g in gene)


def binary_contains(gene: Gene, codon: Codon) -> bool:
    low = 0
    high = len(gene) - 1

    while low <= high:
        mid = (high + low) // 2
        if codon < gene[mid]:
            high = mid - 1
        elif gene[mid] < codon:
            low = mid + 1
        else:
            return True
    return False


class Test(unittest.TestCase):
    def test_short_gene(self):
        gene_str = "ACGTG"
        gene = str_to_gene(gene_str)
        self.assertEqual(len(gene), 1)
        self.assertListEqual(gene, [Codon("A", "C", "G")])

    def test_long_gene(self):
        gene = str_to_gene(GENE_STR)
        self.assertEqual(len(gene), len(GENE_STR) // 3)

    def test_linear_search_exist(self):
        gene = str_to_gene(GENE_STR)
        acg: Codon = Codon("A", "C", "G")
        self.assertTrue(linear_contains(gene, acg))

    def test_linear_search_dont_exist(self):
        gene = str_to_gene(GENE_STR)
        gat: Codon = Codon("G", "A", "T")
        self.assertFalse(linear_contains(gene, gat))

    def test_binary_search_exist(self):
        gene = sorted(str_to_gene(GENE_STR))
        acg: Codon = Codon("A", "C", "G")
        self.assertTrue(binary_contains(gene, acg))

    def test_binary_search_dont_exist(self):
        gene = sorted(str_to_gene(GENE_STR))
        gat: Codon = Codon("G", "A", "T")
        self.assertFalse(binary_contains(gene, gat))


if __name__ == "__main__":
    unittest.main()
