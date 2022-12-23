# Задача 1: Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте разделителем является пробел

# from random import sample


# def list_rand_words(count: int, alp: str = 'абв'):
#     words_list = []
#     for i in range(count):
#         letters = sample(alp, 3)
#         words_list.append("".join(letters))
#     return " ".join(words_list)


# def simple_sentence(words: str) -> str:
#     return " ".join(i for i in words.split() if i != "абв")


# all_list = list_rand_words(int(input("Number of words: ")))
# print(all_list)
# print(simple_sentence(all_list))


# Задача 2: Реализуйте алгоритм сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах


from itertools import groupby, starmap
from os import path


def rle_encode(text="text_words.txt", code_text="text_code_words.txt"):
    if path.exists(text):
        with open(text) as my_f_1, \
                open(code_text, "a") as my_f_2:
            for i in my_f_1:
                my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("The files do not exist in the system!")


def rle_decode(name="text_code_words.txt"):
    if path.exists(name):
        with open(name) as my_f:
            n = ""
            for k in my_f:
                word_nums = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        word_nums.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda x, y: x * y, word_nums)))
    else:
        print("The files do not exist in the system!")


rle_encode(input("Enter the name of the file with the text: "), input("Enter the file name to record: "))
rle_decode(input("Enter the name of the file to decode: "))

