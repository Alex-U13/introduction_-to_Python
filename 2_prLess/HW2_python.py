# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
#     in -> out
# - 6782 -> 23
# - 0.67 -> 13

# n = float(input())
# temp = 0
# if n *100 % 100 == 0:
#     while n // 10 > 0:
#         temp += n % 10
#         n = n // 10
#     print(temp+n)
# else:
#     def fractional_part_len(number_to_count):  # проверка на количество знаков после запятой (самостоятельно не додумалась как можно проверить)
#         count = 0
#         while number_to_count % 1 != 0:
#             number_to_count *= 10
#             count += 1
        
#         return count
#     x = fractional_part_len(n)
#     i = 1
#     while i <= x:
#         n *= 10
#         i = i + 1

#     if n *100 % 100 == 0:
#         while n // 10 > 0:
#             temp += n % 10
#             n = n // 10
#         print(temp+n)


# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

# list_1 = []
# n = int(input("n = "))
# temp = 1

# for i in range(1, (n + 1)):
#     temp *= i
#     list_1.append(temp)
        
# print(list_1)



# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

# list_2 = []
# n = int(input("n = "))

# for i in range(1, (n + 1)):
#     list_2.append((1 + 1 / i)**i)
        
# print(list_2)

# temp = 0
# i = 0
# while i < n:
#     temp += list_2[i]
#     i = i + 1
# print(temp)

# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

# n = int(input("n = "))
# list_3 = []
# for i in range(-n, (n + 1)):
#     list_3.append(i)
# print(list_3)

# pos_1 = int(input("pos_1 = "))
# pos_2 = int(input("pos_2 = "))

# if pos_1 > (n * 2 + 1) or pos_2 > (n * 2 + 1):
#     print("There are no values for these indexes!")
# else:
#     print(list_3[(pos_1-1)] * list_3[(pos_2-1)])


# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

n = int(input("n = "))
list_4 = []
for i in range(0, n):
    list_4.append(i)
print(list_4)


i = 1                                   # не решена!!!!
while i <= n:
    list_4.insert(i, list_4[n-i])
    del(list_4[n-i+1])
    i = i + 1
print(list_4)