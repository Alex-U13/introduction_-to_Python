# # Задача 1: Создайте список из N натуральных чисел (1 до N), упорядоченных по возрастанию.
# # Среди чисел не хватает одного, чтобы выполнялось условие A[i] -1 = A[i-1]
# # Найдите это число

# from random import choice

# n = abs(int(input("n = ")))
# def create_list (max: int):
#     i_list = list(range(max+1))
#     i_list.remove(choice(i_list))
#     return i_list

# def rew(my_list: list):
#     print(my_list)
#     for i in range(1, len(my_list)):
#         if my_list[i] - 1 != my_list[i-1]:
#             return my_list[i] - 1
#     return -1

# print(rew(create_list(n)))


# Задача 2. Создайте список, в который попадают числа, описывающие возрастающую последовательность.
# Порядок элементов нельзя менять


from random import choices


def create_list(n):
    list = choices(range(n*2), k=n)
    return list


second_list_ = create_list(int(input("n = ")))
print(second_list_)


def col(second_list):
    therd_list = []
    for i in range(len(second_list)):
        max = second_list[i]
        list_4 = [max]
        for j in range(i+1, len(second_list)):
            if second_list[j] > max:
                max = second_list[j]
                list_4.append(max)
        if len(list_4) > 1:
            therd_list.append(list_4)
    return therd_list


print(col(second_list_))
