"""
Чтобы получить неглубокую копию, вызовите метод copy
Если нужна глубокая, нужен метод copy.deepcopy.

"""
skils = ["Python", "C", "C++", "SQL"]

user_data_1 = {"name": "Guido van Rossum", "programming_skills": skils}
user_data_2 = user_data_1.copy()

print(user_data_1)
print(user_data_2)

# todo: изучить самостоятельно поверхностное и глубокое копирование в Python
