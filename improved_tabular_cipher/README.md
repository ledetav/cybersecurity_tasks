# 🛡 Improved Tabular Cipher

Реализация улучшенного табличного шифра на Python с юнит-тестами.

## 📚 Описание

Улучшенный табличный шифр представляет собой метод шифрования текста, при котором:
1. Текст записывается в таблицу с фиксированным числом столбцов, определяемым длиной ключа.
2. Столбцы таблицы переставляются согласно порядку букв в ключе.
3. Полученный шифрованный текст извлекается по этим столбцам.

---

## 🚀 Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/ledetav/cybersecurity_tasks.git
cd cybersecurity_tasks/improved_tabular_cipher
```
2. (Опционально) создайте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
```
3. Установите зависимости (если есть):

```bash
pip install -r requirements.txt
```

4. Запустите пример:

```bash
python main.py
```
---

## ✅ Запуск тестов

```bash
python -m unittest discover tests
```

или точечно:

```bash
python improved_tabular_cipher_tests.py
```

Если всё работает, увидите что-то вроде:
```bash
..........
----------------------------------------------------------------------
Ran ?? tests in 0.001s

OK
```
