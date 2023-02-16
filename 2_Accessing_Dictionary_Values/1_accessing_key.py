"""
Обращения к значениям словаря с помощью ключа в квадратных скобках:
dict_top_ten["Китай"]}
"""
from time import sleep

top_ten = {"Россия": "Москва",
                "Канада": "Оттава", 
                "Китай": "Пекин", 
                "США": "Вашингтон", 
                "Бразилия": "Бразилия", 
                "Австралия": "Канберра", 
                "Индия": "Нью-Дели", 
                "Аргентина": "Буэнос-Айрес", 
                "Казахстан": "Астана", 
                "Алжир": "Алжир"}

print(top_ten["Китай"])
sleep(3)
print(top_ten["Индия"])
sleep(5)

# Обратимся по ключу, которого нет!
print(top_ten["Рим"])

