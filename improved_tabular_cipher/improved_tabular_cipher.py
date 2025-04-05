def _order_key(key: str):
    """Возвращает порядок сортировки ключа (напр., KEY -> [1, 0, 2] по алфавиту)"""
    return sorted(range(len(key)), key=lambda k: key[k])

def encrypt_tabular(message: str, key: str) -> str:
    key_order = _order_key(key)
    num_cols = len(key)
    num_rows = (len(message) + num_cols - 1) // num_cols

    # Заполняем таблицу по строкам
    table = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    idx = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if idx < len(message):
                table[r][c] = message[idx]
                idx += 1
            else:
                table[r][c] = ' '  # Заполняем пробелами

    # Считываем по упорядоченным столбцам
    ciphertext = ''
    for col in key_order:
        for row in range(num_rows):
            ciphertext += table[row][col]

    return ciphertext

def decrypt_tabular(ciphertext: str, key: str) -> str:
    key_order = _order_key(key)
    num_cols = len(key)
    num_rows = (len(ciphertext) + num_cols - 1) // num_cols

    # Создаем пустую таблицу
    table = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    # Считаем, сколько символов в каждом столбце
    col_lengths = [num_rows] * num_cols
    total_cells = num_cols * num_rows
    num_padding = total_cells - len(ciphertext)
    for i in reversed(key_order):
        if num_padding > 0:
            col_lengths[i] -= 1
            num_padding -= 1

    # Заполняем таблицу по столбцам
    idx = 0
    for col in key_order:
        for row in range(col_lengths[col]):
            table[row][col] = ciphertext[idx]
            idx += 1

    # Считываем по строкам
    plaintext = ''
    for row in table:
        plaintext += ''.join(row)

    return plaintext.strip()
