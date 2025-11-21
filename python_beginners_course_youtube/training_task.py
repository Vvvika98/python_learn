#сами можем создать модули 

#выбираем из другого файла функции 

from _17_import.math_operations import add, subtract


print(add(1,2))               #импортируемая функция из другого файла сладывает числа
print(subtract(2,1))          #импортируемая функция из другого файла вычитает числа

#либо по другому 

#просто импортировать модуль и уже потом вызывать функции 

from _17_import import math_operations  # noqa: E402

print(math_operations.add(1,2))


# from math_operations import add  # noqa: E402

print(add(1,2))
