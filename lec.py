#                            ДОМАШНЕЕ ЗАДАНИЕ К СЕМИНАРУ 3

# ЗАДАЧА 1. Задайте список из нескольких чисел. Напишите программу, 
#           которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random

# def CreatList(number):
#     number = int(number)
#     list = [i for i in range(-number, number, 3)]
#     return  list

# def Summ(list):
#     result = 0
#     for i in list:
#         if (list.index(i) % 2 > 0):
#             result +=i
#     print(f'The sum of the elements in odd positions is equal to {result}')



# number = input('Enter a positive integer: ')
# list = CreatList(number)
# print(list)
# Summ(list)

# ЗАДАЧА 2. Напишите программу, которая найдёт произведение пар чисел списка.
#           Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def List(array):
#     print(array)
#     firstIndex = 0
#     lasIndex = (len(array)-1)

#     while(firstIndex <= lasIndex):
#         compos = (array[firstIndex])*(array[lasIndex])
#         #print(f'ЧислоЛевое: {array[firstIndex]}, ЧислоПравое: {array[lasIndex]}')

#         print(f'{compos}')
       
#         firstIndex += 1
#         lasIndex -= 1

# List([2,3,5,6])
# List([2,3,4,5,6])

# ЗАДАЧА 3. Задайте список из вещественных чисел. Напишите программу, 
#           которая найдёт разницу между максимальным и минимальным значением 
#           дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# def FloatNumber(array):
    
#     arrayDecimal = []
#     for i in array:
#         if i > 0:
#             dec = round(i % 1 , 3)
#         else:
#             dec = round(i % (-1), 3)
        
#         if dec == 0:
#             continue
#         arrayDecimal.append(dec)

#     print(f'Source elements: {arrayDecimal}')  

#     maximum = max(arrayDecimal)
#     minimum = min(arrayDecimal)

#     print(f'The difference between to {round(maximum - minimum, 3)}')

# FloatNumber([1.1, 1.2, 3.1, 5, 10.01])

# ЗАДАЧА 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Перевод в двоичное (через остаток %)
# 45%2=1, 22%2=0, 11%2=1, 5%2=1, 2%2=0, 1%2=1

# def ToBinar(decimal):
#     result = ''              
#     while decimal > 0:
#         if decimal % 2 == 1:   
#             result += '1'   
#         else:
#             result += '0'   
#         decimal //= 2           

#     return result[::-1]    


# dec = int(input("Enter a positive integer: "))
# print(ToBinar(dec))

# ЗАДАЧА 5. Задайте число. Составьте список чисел Фибоначчи, 
#           в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def Fibonacci(number):
#     if (number < -1):
#         number = -number
#     array = [0, 1]     
#     temp = 1

#     while(temp < number):
#         if number == 1:    
#             print(array)
#             break

#         if number > 1:
#             result = array[len(array)-1] + array[len(array)-2]
#             array.append(result)

#             temp += 1

#     print(f'Fibonacci numbers for {number} = {array}')
#     return  array



# def NegativFibonacci(number):
#     if (number > -1):
#         number = -number

#     array = [0, 1] 

#     temp = -1

#     while(temp > number):
#         if number == -1:
#             print(number)    

#         if(number < -1):

#             result = array[len(array)-2] - array[len(array)-1]
#             array.append(result)

#             temp -=1  

#     print(f'Fibonacci numbers for {number} = {array}')



# number = int(input('Enter a positive integer: '))
# Fibonacci(number)
# NegativFibonacci(number)