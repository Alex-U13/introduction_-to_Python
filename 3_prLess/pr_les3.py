# 1. Задайте список, состоящий из произвольных чисел, количество 
# задает пользователь. Напишите программу, определяющую 
# присутствует ли в заданном списке число, полученное от пользователя.

from random import sample, choices, randint
# print(sample(range(10*2), k=10))  # не выводит дублирующие значения
# print(choices(range(10*2), k=10)) # выводит дублирующие значения
# print(randint(1,9)) # выводит одно случайное изначение из задонного отрезка (мин и макс включительно)

# def createRandomListAndFind(n,num):
#     list=sample(range(1, n*2), k=n)
#     print(list)
#     # if num in list:
#     #     return "YES"
#     # return num in list # возвращает тру или фолс
#     return "YES" if num in list else "NO"

# print(createRandomListAndFind(int(input("n = ")), int(input("num = "))))


# 2. Задайте список, состоящий из произвольных слов, количество задает
# пользователь. Напишите программу, которая определит индекс
# второго вхождения строки в списке либо сообщит, что ее нет

def createRandomList(n):
    list_word = []
    for i in range(n):
        symbol = choices("xyz", k=3)
        list_word.append("".join(symbol))
    return list_word

a = createRandomList(int(input("n = ")))
print(a)

def findWord(word, randomList):
    if randomList.count(word) > 1:
        i = randomList.index(word)
        return randomList.index(word, i+1)  
    else:
        return "не найдено"

print(findWord(input("word - "), a))