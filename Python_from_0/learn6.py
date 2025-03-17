my_string = "Hello, world"
print(my_string)

# строки пишутся в кавычках " " и ' ' , а большой текст в """  """

my_string = """ 
fghjkl;lkjhjklkhjghgfhbjklkgfghjkihjghfgtfhjohghj
kjhgfvgbhjklkijuhygjklkjhghjkl;
lkijuhygfvbnjkl;oiuytgfhnjkloiuytfrgnmj,kl;kijuhygfghjkl
"""
print(my_string)

first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)


# Функция для измерения длинны строки 
lenght = len(full_name)
print(lenght)

print(len("")) 

# из численного типа перевести в строковое
my_integer = 100
my_string = str(my_integer)

print(type(my_string))


# перевод строки в число
my_int = int("10")
print(type(my_int))

# my_int = int("Yo")
# print(type(my_int))
# # выдаст ошибку 

my_string = int(input("Tnter a number: "))
print(type(my_string))


# Задача - посчитать кол-во чисел в огромном числе 
big_integer = 2 ** 1000
print(len(str(big_integer)))


# найти вхождение подстроки в строку
my_string = "Hello, world"

print("hello" in my_string)
# поиск регистрозависимый - это важно 

# метод написания строки КАПСОМ 
my_string = "Alice"
print(my_string.upper())

# метод написания КАПСА прописными буквами 
my_string = "ALICE"
print(my_string.lower())

# удаление лишних пробелов 
my_string = "      Hello, world!      "
print(len(my_string))
print(len(my_string.strip()))

# изменение слова или символа внутри строки 
my_string = "Hello, world!"
print(my_string.replace("world", "Python"))


