"""
Метод setdefault()

Метод setdefault() возвращает значение ключа (если ключ находится в словаре).
Если указанного ключа нет, он вставляет ключ со значением в словарь.

dict.setdefault(key[, default_value])

Метод принимает два параметра:
key - ключ для поиска в словаре;
default_value (необязательно) ‒ ключ со значением default_value вставляется в словарь,
если ключа нет в словаре. Если этот параметр не указан, default_value будет None.


При этом метод возвращает:
- значение ключа, если оно есть в словаре;
- None, если ключа нет в словаре и значение default_value не указано
- default_value, если ключ отсутствует в словаре и указано default_value.

"""

# Пример словаря - рейтинг фильмов
films_rating = {"Властелин колец": 10,
                "Аватар": 10, "Кинг Конг": 9,
                "Гарри Поттер": 9,
                "Форест Гамп": 9.5}


# Вариант 1: мы точно знаем что такой ключ существует:
avatar_rating = films_rating.setdefault("Аватар")
print(f"Рейтинг фильма Аватар: {avatar_rating}")


# Вариант 2: необходимо узнать рейтинг фильма из коллекции данных,
# но если фильма нет, то заносим его без рейтинга:
new_film_rating_2 = films_rating.setdefault("Подмена")
print(new_film_rating_2)
print(f"Обновлённый список фильмов: \n{films_rating}")


# Вариант 3: необходимо узнать рейтинг фильма из коллекции данных,
# но если фильма нет, то заносим его с рейтингом 5:
new_film_rating_3 = films_rating.setdefault("2012", 5)
print(new_film_rating_3)
print(f"Обновлённый список фильмов: \n{films_rating}")


# Вопрос: что если запрос в словарь будет по существующему ключу, но со значением default_value?
# Вариант 4
new_film_rating_4 = films_rating.setdefault("Форест Гамп", 2)
print(new_film_rating_4)
print(f"Обновлённый список фильмов: \n{films_rating}")
