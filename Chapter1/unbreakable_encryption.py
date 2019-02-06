from secrets import token_bytes
from typing import Tuple
import unittest


def random_key(length: int) -> int:
    # generate length random bytes
    tb: bytes = token_bytes(length)
    # convert those bytes into a bit string and return it
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes = original.encode()
    key = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, "big")
    encrypted = original_key ^ key  # XOR
    return key, encrypted


def decrypt(key: int, encrypted_data: int) -> str:
    decrypted = key ^ encrypted_data  # XOR
    temp = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


class Tests(unittest.TestCase):
    def test_encryption_decryption(self):
        text = "Some dummy text that will be encrypted"
        key, encrypted_data = encrypt(text)
        result = decrypt(key, encrypted_data)

        self.assertEqual(result, text)


if __name__ == "__main__":
    unittest.main()
