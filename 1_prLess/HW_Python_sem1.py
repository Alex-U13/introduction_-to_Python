# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет является ли этот день выходным

# print("Введите число (обозначающее день недели, т.е. не более 7): ")
# n = int(input())

# if n>0 and n<6: 
#     print("Workday")
# elif n>5 and n<8:
#     print("Weekend")
# else:
#     print("It's not a day of the week")


# 2. Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if not ((w and z) or (not y) or ((not x) == (not w))):
                        print(x, y, z, w)

# 3. Нaпишите программу, которая принимает на вход координаты точки (X, Y),  
# координаты не равны 0, и выдает номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится)

# print("Введите значение x: ")
# x = int(input())
# print("Введите значение y: ")
# y = int(input())

# if x==0 and y !=0 or x!=0 and y ==0:
#     if x==0: print("На оси Х")
#     elif y==0: print("На оси Y")
# elif x>0 and y >0:
#     print("I четверть")
# elif x<0 and y >0:
#     print("II четверть")
# elif x<0 and y <0:
#     print("III четверть")
# elif x>0 and y <0:
#     print("IV четверть")
# else:
#     print("Error, 0 entered!")


# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y)

# print("Введите номер четверти: ")
# n = int(input())

# if n==1: print("x>0, y>0")
# elif n==2: print("x<0, y>0")
# elif n==3: print("x<0, y<0")
# elif n==4: print("x>0, y<0")
# else: print("The querter is entered incorrectly!")

# 5. Напишите программу, которая принимает на вход координаты точек и 
# находит расстояние между ними в 2D пространстве

# print("Введите x1: ")
# x1 = int(input())
# print("Введите y1: ")
# y1 = int(input())
# print("Введите x2: ")
# x2 = int(input())
# print("Введите y2: ")
# y2 = int(input())

# n = round(((((x2-x1)**2)+((y2-y1)**2))**0.5),3)
# print(n)