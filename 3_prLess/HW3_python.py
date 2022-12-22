from random import sample, choices, uniform

# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).


# def CreateRandomListAndSum(n):
#     list = sample(range(1, n*2), k=n)
#     print(list)
#     temp, i = 0, 0
#     while i < n:
#         temp += list[i]
#         i += 2
#     print(temp)

# print(CreateRandomListAndSum(int(input("n = "))))


# n = int(input("n = "))   # без использования функции
# list_1 = []

# for i in range(n):
#     list_1.append(random.randint(0,5))

# print(list_1)

# temp = 0
# i = 0
# while i < n:
#     temp += list_1[i]
#     i += 2

# print(temp)


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in # 4
# out
# [2, 5, 8, 10]
# [20, 40]            

# def multiplicationOfelements(n):
#     list_2 = choices(range(n), k=n)
#     print(list_2)
#     list_2_new = []
#     for i in range(n//2):
#         list_2_new.append(list_2[i]*list_2[-1-i])
#     if n % 2 != 0:
#         list_2_new.append(list_2[n//2])
#     print(list_2_new)

# print(multiplicationOfelements(int(input("n = "))))



# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011







# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

# def randomFloatList(n):
#     list_3 = []
#     for i in range(n):
#         temp = uniform(0,10)
#         list_3.append(round(temp,2))
#     print(list_3)
#     min, max, i = 100, 0, 0
#     while i < n:
#         if list_3[i] * 100 % 100 < min:
#             min = list_3[i] * 100 % 100
#         if list_3[i] * 100 % 100 > max:
#             max = list_3[i] * 100 % 100
#         i += 1
#     dif = round((max/100 - min/100), 2)
#     print("Min:", min/100, "Max:", max/100, "Difference:", dif)

# print(randomFloatList(int(input("n = "))))


# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5



def fib(n):
    if n in [1,2]:
        return 1
    else:
        return (fib(n-1)) + (fib(n-2))

num = int(input("num = "))
list_5 = []
for i in range(1,num+1):
   list_5.append(fib(i))

# print(list_5)

list_5.insert(0, 0)
#print(list_5)
for i in range(-num,0):
    if i % 2 == 0:
        list_5.insert(0, list_5[i])
    else:
        list_5.insert(0, list_5[i] * (-1))

print(list_5)