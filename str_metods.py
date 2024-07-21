# Объявление
friend='Максим Александрович Попов'
# основные 5 методов строк

# Метод замены
# 1.заменить фамилию на Иванов
print(friend[:21] + 'Иванов')

# 2. замена подстроки строкой
new_friend = friend.replace('Попов', 'Иванов')
print(new_friend)

# 3.  преобразование строки к верхнему регистру
print(friend.upper())

# 4. преобразование в заголовок
print(friend.title())

# 5. Проверка строки -состоит ли из цифр
print(friend.isdigit())

# 6. метод split (разделение строк)
print(friend.split(' '))

bad_data='стол;стул, диван кровать'
print(bad_data.replace(';','').split)