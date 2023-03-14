# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
# 4 

first_numb = 15
second_numb = 9

def sum(a,b):
    if a == 0: 
        if b == 0:
            return 0
        else: return 1+sum(a,b-1)
    else: return 1+sum(a-1,b)
print(sum(first_numb,second_numb))