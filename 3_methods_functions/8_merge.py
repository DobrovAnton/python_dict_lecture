"""
Объединение словарей

- оператор объединения | (доступно для Python 3.9 и выше);
- метод update()
- использование распаковки **
- структура данных collections.ChainMap

Обратить внимание на финальный объединенный словарь, а именно на порядок следования пар ключ-значение
"""

from collections import ChainMap


# Три разных словаря с данными об одном пользователе
user_info_1 = {"name": "Anton", "surname": "Dobrov"}
user_info_2 = {"mobile_phone": "89529270583", "work_phone": None}
user_info_3 = {"age": 32, "marital_status": "married", "hobby": "cooking"}
#
# # Объединение словарей с помощью оператора |:
# user_full_info = user_info_1 | user_info_2 | user_info_3
# print(f"Полная информация о пользователе: \n{user_full_info}")
#
#
# # Объединение двух словарей с помощью метода update():
# user_info_1.update(user_info_2)
# print(f"Информация о пользователе после обновления словаря: \n{user_info_1}")
#
#
# # Объединение словарей с помощью распаковки **:
# user_full_info = {**user_info_1, **user_info_2, **user_info_3}
# print(f"Полная информация о пользователе: \n{user_full_info}")

# Группировка многочисленных словарей с помощью структуры данных collections.ChainMap:
user_full_info = ChainMap(user_info_1, user_info_2, user_info_3)
print(f"\nПолная информация о пользователе: \n{user_full_info}")

print(f"\nкласс данных: {type(user_full_info)}")
print(f"\nрезультат поиска по ключу age: {user_full_info['age']}")


# todo: Задание на самостоятельное изучение и эксперимент:
#  что будет, если объединим словари в которых есть одинаковые ключи с разными значениями?
