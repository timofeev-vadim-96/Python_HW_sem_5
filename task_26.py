# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень 
# B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

first_numb = 3
second_numb = 5

def degree(a,b):
    if b == 0: return 1
    else:
        return a*degree(a,b-1)
print(degree(first_numb,second_numb))
