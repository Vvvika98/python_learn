#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["mom", "dad", "son", "doughter"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [["mom" , 165] , ["dad", 185] , ["son", 170] , ["doughter", 120]]
    # ['имя', рост],


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

print(f"Рост отца - {my_family_height[1][1]} см")


# total = (f"{my_family_height[0][1]} + {my_family_height[1][1]} + {my_family_height[2][1]} + {my_family_height[3][1]}") #ЧТО ЕЩЕ ПЫТАЛАСЬ ДЕЛАТЬ))))))
# print(f"Общий рост моей семьи - {total} см")

height_1 = my_family_height[0].pop() #в квадратных скобках определяю конкретный список из общего списка
# print(height_1)

height_2 = my_family_height[1].pop()
# print(height_2)

height_3 = my_family_height[2].pop()
# print(height_3)

height_4 = my_family_height[3].pop()
# print(height_4)

total_height = height_1 + height_2 + height_3 + height_4

print(f"Общий рост моей семьи - {total_height} см")