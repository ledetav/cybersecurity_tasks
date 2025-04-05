from improved_tabular_cipher import encrypt_tabular, decrypt_tabular

def main():
    print("🔐 Imprived Tabular Cipher")

    examples = [
        {"text": "HELLOENCRYPTION", "key": "KEY"},
        {"text": "THISISASECRETMESSAGE", "key": "SECRET"},
        {"text": "PYTHON", "key": "CIPHER"},
        {"text": "SHORT", "key": "VERYLONGKEY"},
        {"text": "ONE", "key": "A"},
    ]

    for i, example in enumerate(examples, 1):
        text = example["text"]
        key = example["key"]

        encrypted = encrypt_tabular(text, key)
        decrypted = decrypt_tabular(encrypted, key)

        print(f"\nExample {i}:")
        print(f"Original : {text}")
        print(f"Key      : {key}")
        print(f"Encrypted: {encrypted}")
        print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()
