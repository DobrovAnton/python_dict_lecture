"""
В Python включен специализированный подкласс dict, который запоминает порядок вставки добавляемых в него ключей:
collections.OrderedDict.

Хотя в Python 3.6 и выше стандартные экземпляры dict сохраняют порядок вставки ключей,
такое поведение является всего лишь побочным эффектом реализации в Python и не определяется спецификацией языка.
Поэтому, если для работы вашего алгоритма порядок следования ключей имеет значение, лучше всего четко донести эту идею,
задействовав класс OrderDict явным образом.

OrderedDict не является встроенной составной частью базового языка и должен быть импортирован из модуля collections,
находящегося в стандартной библиотеке.
"""

from collections import OrderedDict

numbers = OrderedDict()

numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3
numbers["five"] = 5

print(numbers)

# Метод od.move_to_end(key, last=True) перемещает существующий ключ key в начало/конец упорядоченного словаря.
numbers.move_to_end("one")
print(numbers)

# numbers.move_to_end("five", last=False)
# print(numbers)
