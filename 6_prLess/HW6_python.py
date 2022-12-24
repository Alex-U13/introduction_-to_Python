# Задача 1: Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения котоорых больше предыдущего элемента. Use comprehension

from random import sample

# def more_then(num):
#     my_list = sample(range(num * 3), num)
#     print(my_list)
#     return[my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]


# print(more_then(int(input("n = "))))

# from random import randint

# def more_then(num):
#     original_list = [randint(0, 100) for _ in range(num)]
#     print(original_list)
#     return [num for i, num in enumerate(original_list[1:]) if num > original_list[i]]


# print(more_then(int(input("n = "))))

# Задача 2: Для чисел в пределах от 20 до N найти числа,
# кратные 20 или 21. Use comprehension


# def my_list(num):
#     if num < 20: 
#         print("Введите значение n больше 20")
#         print(my_list(int(input("n2 = "))))
#     else: 
#         return [k for k in range(20, (num + 1)) if k % 20 == 0 or k % 21 == 0]
#     return "Молодец)"

# print(my_list(int(input("n = "))))

# Задача 3: Написать функцию, аргументы - имена сотрудников, возвращает словарь, 
# ключи - первые буквы имен, значения - списки, содержащие имена, начинающиеся с соответствующей буквы


# def thesaurus(*args):
#     names_dict = {}
#     for i in sorted(args):
#         letter = i[0]
#         if letter not in names_dict:
#             names_dict[letter] = [i]
#         else:
#             names_dict[letter] += [i]
#     return names_dict


# print (thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Петр", "Борис"))

from itertools import groupby

def thesaurus(*args):
    if "" not in args:
        return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
    return "Error"


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Петр", "Борис"))