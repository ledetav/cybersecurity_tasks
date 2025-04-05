def caesar_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():  # Проверка, является ли символ буквой
            shift_base = 65 if char.isupper() else 97  # Базовый ASCII для заглавных или строчных букв
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Не изменяем пробелы и знаки препинания
    return encrypted_text


def caesar_decrypt(cipher_text, shift):
    return caesar_encrypt(cipher_text, -shift)  # Дешифровка - это просто инвертированный сдвиг
