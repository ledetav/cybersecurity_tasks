import math

def create_table(text, key):
    cols = len(key)
    rows = math.ceil(len(text) / cols)
    padded_text = text.ljust(rows * cols, '_')
    table = [list(padded_text[i*cols:(i+1)*cols]) for i in range(rows)]
    return table

def encrypt(text, key):
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    table = create_table(text, key)
    ciphertext = ''
    for index, _ in key_order:
        for row in table:
            ciphertext += row[index]
    return ciphertext

def decrypt(ciphertext, key):
    cols = len(key)
    rows = math.ceil(len(ciphertext) / cols)
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    
    table = [[''] * cols for _ in range(rows)]
    index = 0
    for k, _ in key_order:
        for r in range(rows):
            table[r][k] = ciphertext[index]
            index += 1
    return ''.join([''.join(row) for row in table]).rstrip('_')
