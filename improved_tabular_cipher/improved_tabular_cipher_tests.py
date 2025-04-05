import unittest
from cipher import encrypt, decrypt

class TestEnhancedTableCipher(unittest.TestCase):

    def test_encrypt_returns_correct_cipher(self):
        message = "HELLOENCRYPTION"
        key = "KEY"
        expected_length = len(message)
        result = encrypt(message, key)
        self.assertEqual(len(result), expected_length)

    def test_decrypt_returns_original_message(self):
        message = "HELLOENCRYPTION"
        key = "KEY"
        encrypted = encrypt(message, key)
        decrypted = decrypt(encrypted, key)
        self.assertEqual(decrypted, message)

    def test_encrypt_with_padding(self):
        message = "TEST"
        key = "LONGKEY"
        encrypted = encrypt(message, key)
        self.assertTrue('_' in encrypted)

    def test_decrypt_removes_padding(self):
        message = "TEST"
        key = "LONGKEY"
        encrypted = encrypt(message, key)
        decrypted = decrypt(encrypted, key)
        self.assertEqual(decrypted, message)

    def test_encrypt_empty_string(self):
        self.assertEqual(encrypt("", "KEY"), "")

    def test_decrypt_empty_string(self):
        self.assertEqual(decrypt("", "KEY"), "")

    def test_encrypt_single_char(self):
        self.assertEqual(encrypt("A", "B"), "A")

    def test_decrypt_single_char(self):
        self.assertEqual(decrypt("A", "B"), "A")


if __name__ == '__main__':
    unittest.main()
