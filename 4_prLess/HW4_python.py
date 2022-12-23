# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

# def accuracy(num, d):
#     decimal_place_num = len(num) - num.index(".") - 1
#     decimal_place_d = (len(d) - 2)

#     if decimal_place_num == decimal_place_d:
#         return num
#     elif decimal_place_num < decimal_place_d:
#         temp = decimal_place_d - decimal_place_num
#         return num + '0'*temp
#     else: 
#         temp = decimal_place_num - decimal_place_d
#         return num[:-1*temp]

# print(accuracy(input("num = "), input("d = ")))


# from decimal import Decimal

# num = Decimal(input("n = "))
# num = num.quantize(Decimal("0.001"))
# print(num)


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей 
# числа N.
# in 54  out  [2, 3, 3, 3]


# n = int(input("N: "))
# list_of_multipliers = []
# d = 2
# while d * d <= n:
#         if n % d == 0:
#             list_of_multipliers.append(d)
#             n = n // d
#         else:
#             d += 1
# list_of_multipliers.append(n) 
# print(list_of_multipliers)


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import choices

def CreateRandomList(n):
    if n < 0:
        print("Negative value of the number of numbers!")
    else: 
        list_1 = choices(range(1, n), k=n)
        print(list_1)
        temp = []
        for i in list_1:
            if list_1.count(i) == 1:
                temp.append(i)       #выдает ошибку. Почему не знаю. Можете подсказать? 
        print(temp)

print(CreateRandomList(int(input("n = "))))

# При решении задачи 3 логика была сл.:
# Создаю список при помощи choices далее делаю проверку на количество вхождений i-го элемета 
# первого списка. Если количество вхождений == 1, то записываю этот элемент в новый список. 
# далее вывод нового списка без повторяющихся элементов



# * 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
#  записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0










# ** 5. Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"

# out
# The contents of the files do not match!