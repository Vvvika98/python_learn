#КОРТЕЖИ - неизменяемые 

user_roles = ("admin", "editor", "viewer") 


#длина строки
#итерация по циклам
#вхождение in, not in
#нотация срезов, индексация 
#кортеж из одного экземпляра ("ф",)
#распаковка кортежа с помощью множественого присваивания (но кол-во переменных должно быть равно кол-ву элементов в кортеже)
#используем кортеж только когда уверены, что структуру данных не нужно будет менять


#---------------------------------------------------------------------------------------------

#СЛОВАРИ - пара клюк:значеине

person = {
    "name" : "John",
    "age" : 30,
    "city" : "New York"
}

#1    добавление элементов в соварь 
person["job"] = "Engineer"


#2    пустой словарь 
person_1 = {}

#3    значения соваря можно вызывать по ключу 
print(person["name"])
 
#но если запросить ключа, которого нет - ОШИБКА 
#можем использовать метод и тогда ошибки не будет 
print(person.get("name"))
print(person.get("country", "USA")) #none по умолчанию, либо через запятую указать дефолтное значение 


#4    можем итерироваться только по ключам/значениям или по ключам и значениям
for item in person.items():  #распаковка в виде пары ключ-значение в виде кортежа 
    key, value = item        #распковка множественным присваиванием 
    print(item) 
    print(key)
    print(value)
#или сделать это сразу 
for key, value in person.items():
    print(key)
    print(value)


#если только по ключам ДЛЯ БОЛЕЕ ЯВНОГО ИСПОЛЬЗУЮ МЕТОД 
for key in person.keys():
    print(key)

#если только по значениям ДЛЯ БОЛЕЕ ЯВНОГО ИСПОЛЬЗУЮ МЕТОД 
for value in person.values():
    print(value)

#4    СРАВНЕНИЕ СЛОВАРЕЙ (т.к. ключи уникальны - порядок не имеет значения)
#если хотя бы озно значение будет другим - вернется False 
#если будет разное кол-во ключей - вернется False 

pers = {

    "name" : "John",
    "age" : 30,
    "city" : "New York"
}

other_pers = {
    "city" : "Moscow",
    "age" : 30,
    "name" : "John"
}
print(pers == other_pers)


#объединение словарей 
per = {

    "name" : "John",
    "age" : 30,
    "city" : "New York"
}

additional_person_info = {
    "job" : "Engineer",
    "married" : True, 
    "city" : "London"
}
per.update(additional_person_info)
print(per)   #значеине СИТИ возьмет из последнего объекта 

#второй вариант 
per = per | additional_person_info
print(per)   #значеине СИТИ возьмет из последнего объекта 


#---------------------------------------------------------------------------------------------

#  homework 
# Есть список словарей со студентами `students`. В каждом объекте есть имя и фамилия студента,
# а также список оценок (целых чисел). Нужно написать функцию get_best_students, которая берёт студентов и находит того,
# у кого средний балл наибольший. Возвращает функция список студентов с лучшим баллом. У некоторых студентов в оценках
# есть None: их среднюю оценку мы считаем равной 0.

def get_best_students(students):
    result = []
    best_average_grade = 0
    average = 0
    for student in students:               #перебираем каждый словарь  
        if student["grades"] is None:
            average = 0
        else:
            average = sum(student["grades"]) / len(student["grades"])    #нахождение среднего арифметического 
        if average > best_average_grade:
            best_average_grade = average
            result.append(student)
        elif best_average_grade == average:
            result.append(student)
    return result
    


students = [
    {"name": "John", "surname": "Doe", "grades": [5, 5, 4, 4]},
    {"name": "Jane", "surname": "Doe", "grades": [4, 3, 4, 3, 5]},
    {"name": "Bill", "surname": "Gates", "grades": [5, 5, 5, 3]},
    {"name": "Steve", "surname": "Jobs", "grades": [3, 5, 4, 3, 3, 5]},
    {"name": "Guido", "surname": "Van Rossum", "grades": [5, 3, 5, 4, 5, 5, 3, 5]},
    {"name": "Elon", "surname": "Musk", "grades": None}

]

print(get_best_students(students=students))  
# Outputs: [{'name': 'John', 'surname': 'Doe', 'grades': [5, 5, 5, 4]}, {"name": "Bill", "surname": "Gates", "grades": [5, 5, 5, 3]}]

