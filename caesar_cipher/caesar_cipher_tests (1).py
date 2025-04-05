import unittest
from caesar_cipher import caesar_encrypt, caesar_decrypt

class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_lowercase(self):
        self.assertEqual(caesar_encrypt("abc", 3), "def")

    def test_encrypt_wraparound(self):
        self.assertEqual(caesar_encrypt("xyz", 3), "abc")

    def test_encrypt_uppercase(self):
        self.assertEqual(caesar_encrypt("HELLO", 3), "KHOOR")

    def test_encrypt_with_punctuation(self):
        self.assertEqual(caesar_encrypt("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_decrypt_basic(self):
        self.assertEqual(caesar_decrypt("def", 3), "abc")

    def test_decrypt_wraparound(self):
        self.assertEqual(caesar_decrypt("abc", 3), "xyz")

    def test_decrypt_uppercase(self):
        self.assertEqual(caesar_decrypt("KHOOR", 3), "HELLO")

    def test_decrypt_with_punctuation(self):
        self.assertEqual(caesar_decrypt("Mjqqt, Btwqi!", 5), "Hello, World!")

    def test_encrypt_shift_26(self):
        self.assertEqual(caesar_encrypt("abc", 26), "abc")

    def test_encrypt_shift_27(self):
        self.assertEqual(caesar_encrypt("abc", 27), "bcd")

if __name__ == "__main__":
    unittest.main()
