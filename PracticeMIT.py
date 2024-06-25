print('Date: 25.06.2024')
print('Practice: Mutable and Immutable Objects. Tuples')
# 2.
immutable_var = 'Date', 'Name', 1, 2, 2.1, 2.2, False, True
print(immutable_var)
print(type(immutable_var[0]), type(immutable_var[2]), type(immutable_var[5]), type(immutable_var[6]))
# 3.
# immutable_var[0] = 'Дата'
# print(immutable_var) - TypeError: 'tuple' object does not support item assignment
# Объясните, почему нельзя изменить значения элементов кортежа.
# Кортеж служит для создания неизменной коллекции элементов,
# можно выводить значения по индексам, можно слагать, умножать (повторять) коллекции кортеждей, но нельзя менять ни состав, ни последовательность
# Внутри кортежа, однако, можно создать список и с этим списком можно делать все операции для списка, даже менять состав элементов
# Например:
immutable_var = ['Date', 'Дата'], 'Name', 1, 2, 2.1, 2.2, False, True
immutable_var[0].remove('Date') # удалять
print(immutable_var) # (['Дата'], 'Name', 1, 2, 2.1, 2.2, False, True)
immutable_var[0][0]='Date' # заменять в составе списка
print(immutable_var) # (['Date'], 'Name', 1, 2, 2.1, 2.2, False, True)
immutable_var[0][0]='Month' # вводить новые строки, полностью заменяя список
print(immutable_var) # (['Month'], 'Name', 1, 2, 2.1, 2.2, False, True)
# 4.
mutable_var = ['Date' 'Name', 1, 2, 2.1, 2.2, False, True]
mutable_var[0]='Month' # замена
mutable_var.append('End') # дабавление
print(mutable_var) # вывод на экран замены и добавления
print(mutable_var[::-1]) # изменение последовательгости и вывод на экран

