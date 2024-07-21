# объявление
ofice = {'max', 'kate', 'john', 'leo'}
freelance = {'max', 'kate', 'poli'}

#  основные 5 методов

# 1. вычитание одного из другого множества
#  выделение тех, кто работает только в офисе
print(ofice-freelance)

# 2 выделение тех, кто работает только на фрилансе
print(freelance-ofice)

# 3.  выделение тех, кто работает и в офисе и на фрилансе (и там и там) -(пересечение)
print(ofice&freelance)

# 4. объединение
print(ofice|freelance)

# 5. использование  for
for item in ofice:
    print(item)
