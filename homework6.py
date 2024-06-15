my_dict = { 'Olya' : 1975, 'Julia' : 1941, 'Oleg' : 1964  }
print(my_dict)
print( my_dict.get('Olya'))
print( my_dict.get('Nina', 'такого ключа нет'))
my_dict.update ({'Kolya' : 1980,
                 'Olesya' : 1988})
print(my_dict)
my_dict.pop('Kolya')
print(my_dict)

my_set = {1, 2, 3, 1, 2, 3, 'Apple', 'Apple' }
print(my_set)
print(my_set.add(5))
print(my_set.add('Nina'))
print(my_set)
print(my_set.discard(1))
print(my_set)

