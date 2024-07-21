# словарь, объявление
name = "max"
age = 20
has_car = True
friend = (name, age, has_car)
friend = {
    'name': 'max',
    'age': 20,
    'has car': True
}
print(type(friend))

 # Основные 5 методов словаря

# 1. Добывить
friend['has_wife']= False
print(friend)

# 2. Изменить
friend['has_wife']= True
print(friend)

# 3. Удалить
del friend['has_wife']
print(friend)

# 4. получить ключи
print(friend.keys())
#  или получить ключи в виде списка
print(list(friend.keys()))

# 5. Получить значения
print(friend.values())
#  или получение значения в виде списка
print(list(friend.values()))

# 6. Получить пары: ключ-значение (кортежи)
print(friend.items())
#  или получить пары:ключ-значение в виде списка
print(list(friend.items()))
