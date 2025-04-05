from caesar_cipher import caesar_encrypt, caesar_decrypt

# Пример шифрования
encrypted_text = caesar_encrypt("Hello, World!", 3)
print(encrypted_text)  # Выведет "Khoor, Zruog!"

# Пример дешифрования
decrypted_text = caesar_decrypt(encrypted_text, 3)
print(decrypted_text)  # Выведет "Hello, World!"