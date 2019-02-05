import unittest
from sys import getsizeof
from random import choices
from typing import Dict, List


CompressMapper = Dict[str, int]
DecompressMapper = Dict[int, str]

NUCLEOTIDES = "ACGT"


class CompressedGene:
    compress_mapping: CompressMapper = {k: i for i, k in enumerate(NUCLEOTIDES)}
    decompress_mapping: DecompressMapper = {i: k for i, k in enumerate(NUCLEOTIDES)}

    def __init__(self, gene: str) -> None:
        self.bit_string = self.compress(gene)

    def compress(self, gene: str) -> int:
        bit_string: int = 0  # start with sentinel
        for nucleotide in gene.upper():
            bit_string <<= 2  # shift left two bits
            bit_string |= self.compress_mapping[nucleotide]
        return bit_string

    def decompress(self) -> str:
        gene: List[str] = []
        for i in range(0, self.bit_string.bit_length(), 2):
            bits = self.bit_string >> i & 0b11
            gene.append(self.decompress_mapping[bits])

        return "".join(reversed(gene))

    def __repr__(self) -> str:
        return self.decompress()


class Tests(unittest.TestCase):
    def test_compress(self):
        original = "".join(choices(NUCLEOTIDES, k=1000))
        compressed = CompressedGene(original)

        self.assertEqual(getsizeof(original), 1049)
        self.assertEqual(getsizeof(compressed.bit_string), 292)
        compress_ratio = getsizeof(compressed.bit_string) / getsizeof(original)
        self.assertAlmostEqual(compress_ratio, 0.28, places=2)

    def test_equality(self):
        original = "".join(choices(NUCLEOTIDES, k=10))
        compressed = CompressedGene(original)

        self.assertEqual(original, str(compressed))


if __name__ == "__main__":
    unittest.main()
