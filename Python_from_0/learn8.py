fruits = ["apple" , "banana" , "cherry" , "watermelon"]

print(fruits[0])
print(fruits[-4])
print(fruits[3])


# индексы 0,1,2,3 или -4, -3, -2, -1


# можно делать присвоение в список, как в переменную
fruits = ["apple" , "banana" , "cherry" , "watermelon"]
fruits[0] = "pineapple"

print(fruits)


# можно сделать перестановку элементов в списке 
fruits = ["apple" , "banana" , "cherry" , "watermelon"]
fruits[0], fruits [3] = fruits [3] , fruits [0]
print(fruits)


# СЛАЙСЫ
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:5])
# выбрать первые пять элементов 

# их можно присвоить в новый список
new_numbers = numbers[0:5]
print(new_numbers)

# если хотим длину всего списка (полный список)
new_numbers = numbers[:]
# 0 и len() поставятся автоматически
print(new_numbers)


# слайсы можно сделать с шагом 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = numbers[0:10:2]
# запись эквивалента вот такой:
# new_numbers = numbers[::2]
print(new_numbers)


# для слайсов можно использовать отрицательные значения от -1 и далее (но считаем справа налево) т.е. 9 = -1, 8 = -2 и т.д.


# слайсы можно разворачивать в обратном порядке используя:
new_numbers = numbers[::-1]


# тоже самое можно делать и со строками 
string = "Hello, world"

print(string[5:])

# три способа для разворота листа 

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# первый способ new_numbers = numbers[::-1]
# второй способ - использовать метод .reverse()
# третий способ - использовать встроенную функцию, обернув ее в функцию лист
new_numbers = list(reversed(numbers))
print(type(new_numbers))
print(new_numbers)