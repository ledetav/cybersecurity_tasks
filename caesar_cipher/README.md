# 🛡 Caesar Cipher

Реализация классического шифра Цезаря на Python с юнит-тестами.

## 📚 Описание

Шифр Цезаря — один из самых простых методов шифрования. Каждый символ заменяется на символ, находящийся на фиксированное число позиций дальше в алфавите.

Поддержка:
- верхнего и нижнего регистра,
- знаков препинания (не шифруются),
- шифрование и дешифрование.

---

## 🚀 Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/caesar_cipher_project.git
cd caesar_cipher_project
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
python tests/test_cipher.py
```

Если всё работает, увидите что-то вроде:
```bash
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
```
