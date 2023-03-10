"""
Методы словарей:

items() - возвращает все ключи в словаре и связанные с ними значения в виде последовательности кортежей.

keys() - возвращает все ключи в словаре в виде последовательности кортежей.

values() - возвращает все значения из словаря в виде последовательности кортежей

"""

from time import sleep

phone_book = {"Кристина": "8-800-001",
              "Алина": "8-500-002",
              "Регины": "8-600-003",
              "Мария": "8-777-555"
              }
print()
sleep(5)

print(f"Метод tems:\n{phone_book.items()}", "\n")
sleep(10)

print(f"Метод keys:\n{phone_book.keys()}", "\n")
sleep(10)

print(f"Метод values:\n{phone_book.values()}")

# # Пример использования метода items()
# for k, v in phone_book.items():
#     print(f"Имя: {k}\n"
#           f"Телефон: {v}\n")
