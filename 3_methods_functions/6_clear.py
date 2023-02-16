"""
Метод clear()

clear() - возвращает все ключи в словаре и связанные с ними значения в виде последовательности кортежей.

"""

from time import sleep

phone_book = {"Кристина": "8-800-001",
              "Алина": "8-500-002",
              "Регины": "8-600-003",
              "Мария": "8-777-555"
              }

phone_book.fromkeys()

# Важно! Этот метод не возвращает никаких значений!
print(f"Метод clear:\n{phone_book.clear()}", "\n")
