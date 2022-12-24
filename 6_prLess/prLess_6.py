# Красивое решение задачи 1 семинара 4

# from  decimal import Decimal

# def accuracy(num, acc):
#     number = Decimal(f"{num}")
#     return number.quantize(Decimal(f"{acc}"))


# print(accuracy(float(input("Enter a real number: ")), float(input("Enter the required accuracy 0.0001: "))))

# num = float(input(" number float: "))

# my_list = input("enter therequired accuracy '0.0001': ").split(".")
# print(my_list)
# _, accu = my_list                       # _ - безымянная перемення, которая в дальнейшем не исп-ся. В данном примере целая часть числа
# print(f"{num:.{len(accu)}f}")


# Задача на семинар: Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,* приоритет операций стандартный.

actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}


def form(my_list: list):
    # my_list = string.split()
    elements = []
    i = 0
    while i < len(my_list):
        if my_list[i] == "(":
            if "(" in my_list[i+1:]:
                my_list = my_list[:i+1] + form(my_list[i+1:])
            k = my_list.index(")", 1)
            elements.append(my_list[i+1: k])
            i = k
        else:
            elements.append(my_list[i])
        i += 1
    return elements


def result(list_elemens: list):
    for j, k in enumerate(list_elemens):
        if isinstance(k, list):
            list_elemens[j] = result(k)
    r_list = [i for i, v in enumerate(list_elemens) if v in "*/"]
    count_list = []
    while r_list:
        index_op = r_list[0]
        a, b, c = list_elemens[index_op - 1 : index_op + 2]
        list_elemens[index_op - 1 : index_op + 2] = [actions[b](a,c)]
        r_list = [i for i, v in enumerate(list_elemens) if v in "*/"]
    while len(list_elemens) > 1:
        a, b,c = list_elemens[:3]
        list_elemens[:3] = [actions[b](a,c)]
    return list_elemens[0]


print(result(form("8 + 2 * 4 + ( 6 + (2 - 3 * 7 + ( 77 - 11 ) ) * 2".split())))
print(8 + 2 * 4 + ( 6 + (2 - 3 * 7 + ( 77 - 11 ) ) * 2))