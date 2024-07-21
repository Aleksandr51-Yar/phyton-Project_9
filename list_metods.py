friends=['max', 'kate', 'john', 'leo']

# Основные 5 методов списка


# 1. Добавление
friends.append('poll')
print(friends)

# 2 Изменение
friends.insert(3, 'maria')
print(friends)

# 3. Удаление
friends.remove('maria')
print(friends)

# 3а Удаление по индексу
del friends[3]
print(friends)

# 4. Сортировка (по алфавиту)
friends.sort()
print(friends)

# 5.  Сортировка в обратном порядке
friends.reverse()
print(friends)

