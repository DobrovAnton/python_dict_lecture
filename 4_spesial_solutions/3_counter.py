"""
Counter

Объект класса Counter полезен, когда нужно получить количество повторов объектов итерируемой сущности.
"""

from collections import Counter

the_string = "AABCBBCAACBCABBABABBACCACBCBBBCA"
the_counter = Counter(the_string)
print(f"Статистика: \n"
      f"{the_counter}")

print(the_counter["B"])

