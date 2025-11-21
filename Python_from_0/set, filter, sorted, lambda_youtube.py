#уникальные неупорядоченные элементы 

# задача - убрать из списка повторящие цифры

numbers = [1,2,2,3,4,4,4,5,6,6,7]

# unique_numbers = set(numbers)
# unique_numbers = list(unique_numbers)

unique_numbers = list(set(numbers))

print(unique_numbers)


#множества и словари похожи, но множества - это только ключи, а словари пары = ключ-знчение

#-------------------------------------------------------------------------


#ФУНКЦИИ sorted filter


##################sorted#################
#дефолтные (по умолчанию) сортировки идут от меньшего к большему

fruits = ["banana", "apple","cherry", "date"]

sorted_fruits = sorted(fruits)  #по алфавиту по умолчанию от меньшего к большему)

print(sorted_fruits, fruits) #первоначальный не меняется 

# в обратную сторону 

sorted_fruits = sorted(fruits, reverse=True) 
print(sorted_fruits, fruits)


#добавив  ключ сортировки меняем смысл сортировки 

# создаем функцию, которая сортирует элементы по длинне 
def sort_by_len(element: str) -> int:
    return len(element)

sorted_fruits = sorted(fruits, key=sort_by_len)  #поскольку в другие функции можно парадавать функции в качестве аргументов, мы передали в качестве ключа функцию высчитывающую длину элемента

# сначала найдется длина каждого элемента а затем уже произойдет сортировка по длине от меньшего к большему
print(sorted_fruits) #['date', 'apple', 'banana', 'cherry']

#ДАН СПИСОК - НАДО СЛОВАРИ отсортировать по возрасту людей

people = [
    {"name" : "Alice", "age" : 25},
    {"name" : "Diana", "age" : 30},
    {"name" : "Bob", "age" : 20},
    {"name" : "Charlie", "age" : 30}
    
]

def sort_by_age(person: dict) -> int:
    return person["age"]  #вернет значение ключа возраст

sorted_people = sorted(people, key=sort_by_age)
print(sorted_people)

#ЕСЛИ НЕОБХОДИМА СОРТИРОВКА СРАЗУ ПО ДВУМ ПРИЗНАКАМ 
#условимся, что если однаковый возраст - сделать еще сортировку по алфавиту 

def sort_by_age_name(element: dict) -> tuple[int, str]:
    return element["age"], element["name"]

sorted_people = sorted(people, key=sort_by_age_name)
print(sorted_people)


##################filter#################
#в фильтрации ключ должна возвращать значение буул Тру или Фолс

def is_even(n: int) -> bool:
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filtered_numbers = list(filter(is_even, numbers))   #пишется сначала функция-ключ, а затем массив, который необходимо отфильтровать
#но результат надо оборачивать в список, т.к. само значение функции фильтр не читаемо 

print(type(filtered_numbers))
print(filtered_numbers)


people_1 = [
    {"name" : "Alice", "age" : 17},
    {"name" : "David", "age" : 40},
    {"name" : "Bob", "age" : 30},
    {"name" : "Charlie", "age" : 19}
    
]

# нужно отфитровать людей, которым больше 18ти

def is_adult(person: dict) -> bool:
    return person["age"] >= 18


filtered_people = list(filter(is_adult, people_1))

print(filtered_people)

#-------------------------------------------------------------------------

#lambda функции 

# чтоб не загромождать код, например, когда нужны функции-ключи для функций фильтр и сортед 

def sort_by_len(element: str) -> int:
    return len(element)


#тоже самое только с лямбдой функцией 

sort_by_len_lambda = lambda element : len(element) #вместо def = lambda названия функции нет и через : то, что она возврашает

#смотрим выводы обеих функций 

print(sort_by_len("banana"))
print(sort_by_len_lambda("banana"))

#есть массив фруктов, который мы хотим отсортироват по длине 
fruits_1 = ["banana", "apple","cherry", "date"]

sorted_fruits_1 = sorted(fruits_1, key = lambda element: len(element), reverse=True)

print(sorted_fruits_1)

#лямбда функции можно втавлять в другие втсроенные функции питона, например max, min, map и т.д.abs

# функция max вернула один жлемент из этой выборке - самое длинное слово 


longest_words = max(fruits_1, key = lambda element : len(element))

print(longest_words)


#-------------------------------------------------------------------------

#HOMEWORK 

#  задание
#  напишите сортировку с лямбдой, которая вернёт минимальный элемент из списка `people`, сортировка должна быть
#  сначала по возрасту, а потом по имени


people_2 = [
    {"name": "Alice", "age": 25},
    {"name": "Charlie", "age": 20},
    {"name": "Bob", "age": 20},
    {"name": "Diana", "age": 30},
]

sorted_people = min(people_2, key= lambda element : (element["age"], element["name"]))
print(sorted_people)