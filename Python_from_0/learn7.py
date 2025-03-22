fruits = ["apple" , "banana" , "cherry"]
print(fruits)
# вывел список фруктов 

# списки можно создавать по другому 
my_list = list()
print(my_list)
# в таком случае вывод даст пустой список 

# чтобы узнать блину списка - функция len (считает по количеству элементов в списке)
fruits = ["apple" , "banana" , "cherry"]
print(len(fruits))


# в списке могут лежать не только однородные данные (спискиб инты,флоты, буллы, другие списки и т.д.)
my_list = ["apple" , 1 , 1.5 , True, [1, 2, 3]] 
print(my_list)
# НО! Так лучше не делать и держать в списке какой-то однородный  тип данных

# списки можно сравнивать друг с другом 
my_list1 = [1, 2, 3]
my_list2 = [1, 3, 2]
my_list3 = [1, 2, 3]

print(my_list1 == my_list2) 
# списки не равны 

print(my_list1 == my_list3) 
# списки равны 


# в списик можно передавать функцию bool, чтобы использовать их в выражениях с if
print(bool([]))
print(bool([0]))


# Посмотреть то или иное значение в списке 
fruits = ["apple" , "banana" , "cherry"]
print("banana" in fruits)

print("watermelon" in fruits)


# есть переменные и нужно создать их них список 
element1 = "apple" 
element2 = "banana"
element3 = "cherry"

fruits = [element1 , element2 , element3]
print(fruits)


# Списки можно создавать из сторок 
world = "hello"
my_list = list(world)
print(my_list)
# вывел каждую букву в отдельный элемент списка 


# Списики можно складывать друг с другом 
my_list1 = [1 , 2 , 3]
my_list2 = [4 ,5, 6]
my_list3 = my_list1 + my_list2
print(my_list3)

# У списков есть определенное колличество методов 
fruits = ["apple" , "banana" , "cherry"]
fruits.append("watermelon")
print(fruits)
# главное отличие списков от строк в том, что в списке меняется первоначальная переменная, 
# а в строках мы заменяем слово, но это уже другая переменная, пример:
my_string = "hello, world"
new_string = my_string.replace("world" , "python")

print(my_string)
print(new_string)

# удаление последнего элемента списка и присвоение его в новую переменную
fruits = ["apple" , "banana" , "cherry"]
fruit = fruits.pop()
print(fruit)
print(fruits)
# а если не присваивать последний элемент списка в новую переменную, 
# список будет изменен - просто выдаст без последнего значение 


fruits = ["apple" , "banana" , "cherry"]
fruits2 = ["fig" , "grape"]

fruits.extend(fruits2)
print(fruits)
# метод добавления второго списка к первому 
# ????А ЧЕМ ОН ОТЛИЧАЕТСЯ ПРИМЕНЕНИЕ ОТ ОБЫЧНОГО СЛОЖЕНИЯ СТРОК?????


# метод разворачивания списка
fruits = ["apple" , "banana" , "cherry"]

fruits.reverse()
print(fruits)


# отсортировать список (по возратсанию)
my_list = [5 , 4 , 8 , 10 , 1 , 2, 4, 14]
my_list.sort()
print(my_list)


# отсортировать список (по убыванию)
my_list = [5 , 4 , 8 , 10 , 1 , 2, 4, 14]
my_list.sort(reverse=True)
print(my_list)


# создать список из строк, разделенных пробелом из этой строки
my_string = "My name is Alex"
my_list = my_string.split(" ")
print(my_list)


# наоборот собрать из списка строку
joined_string = " ".join(my_list)
print(joined_string)

# В списки можно передавать в различные встроенные функции, которые работают с числами, строками и т.д

my_list = [5 , 4 , 8 , 10, 1 , 2 , 14 , 4]
print(max(my_list))
# максимальный элемент в списке 

my_list = [5 , 4 , 8 , 10, 1 , 2 , 14 , 4]
print(min(my_list))
# минимальный элемент

my_list = [5 , 4 , 8 , 10, 1 , 2 , 14 , 4]
print(sum(my_list))
# сумма элементов 


