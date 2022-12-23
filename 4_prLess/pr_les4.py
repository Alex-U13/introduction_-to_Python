# 1. Задайте строку из набора чисел. Напишите программу, 
# которая покажет большее и меньшее число. В качестве разделителя используйте пробел.

# text = input("Введите набо чисел чере пробел: ")
# def cleaner(string: str):
#     list_1 = string.split()
#     for i, item in enumerate(list_1):
#         list_1[i] = item.strip('.,:!/*+')
#         if not list_1[i].replace("-", "").isdigit():
#             print("Incorrect data")
#             return []
#     return list_1

# def diff(list_for_diff: list):
#     if list_for_diff:
#         min_value = min(list_for_diff, key=int)
#         max_value = max(list_for_diff, key=int)
#         return min_value, max_value
#     return 0, 0


# user_input = input("число: ")
# imput_list = cleaner(user_input)
# min_val, max_val = diff(imput_list)
# print(f"Min value = {min_val}, max value = {max_val}")

# 2. Найдите корни квадратного уравнения Ax**2 + Bx + C = 0,
# с помощью модуля. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл


from math import sqrt

def discr(a: int, b: int, c: int):
    res = b**2-4*a*c
    with open("newFile.txt", "a", encoding="utf-8") as file:
        if res > 0:
            sqr1 = (-b+sqrt(res)) / (2*a)
            sqr2 = (-b-sqrt(res)) / (2*a)
            file.writelines([f"{sqr1}, {sqr2}\n"])
        elif res == 0:
            sqr3 = (-b)/ (2*a)
            file.write(f"{sqr3}\n")
        else: 
            file.write("нет корней\n")

for i in range(int(input("сколько раз выгрудать -"))):
    a, b, c = int(input("a = ")), int(input("b = ")), int(input("c = "))
    discr(a,b,c)


# 3. Задайте 2 числа. Напишите программу, которая находит 
# наименьшее общее кратное этих двух чисел
# # 14 18 -> 126, 17 11 -> 187

# from math import gcd

# def nok(a, b):
#     return a * b // gcd(a, b)

# print(nok(int(input("a = ")), int(input("b = "))))