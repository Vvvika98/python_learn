import datetime   #импортируем модуль


utc_time = datetime.datetime.now(datetime.UTC)         #достаем время ютиси
print(utc_time) #выводим это время 


current_datetime = datetime.datetime.now() #текущее время
print(current_datetime)

#методы

#исо формат - отделяет дату и время буквой Т между собой 
print(current_datetime.isoformat())
print(current_datetime.month)   #вызвать составляющие объекта "время" - месяц
print(current_datetime.year)   #вызвать составляющие объекта "время" - год
print(current_datetime.day)   #вызвать составляющие объекта "время" - день
print(current_datetime.hour) #час
print(current_datetime.minute) #минута


#-------------------------------------- 
#еще вариант 

some_datetime = datetime.datetime(year=2021, month=5, day=1, hour=12, minute=30)

print(some_datetime)

#------------------------------------
# работа с датой

current_date = datetime.date.today() #метод today()
print(current_date)   #без часов 


#вытащить дату из даты-время

current_date_2 = current_datetime.date() #метод date()
print(current_date_2)

#объект дата-время сутки назад

day_ago = current_datetime - datetime.timedelta(days=1)
print(day_ago)

#метод для более читаемого формата дата-время

print(current_datetime.strftime("%A, %d %B %Y"))  #Thursday, 02 October 2025


#дата в исо формате преобразовать в формат дата-время чтоб редактировать 
isoformat = "2023-08-07T20:15:30.384294"

my_datetime = datetime.datetime.fromisoformat(isoformat)
print(type(my_datetime))
print(my_datetime)


#----------------------------------------------------------------------------------------------------

#РАБОТА С ФАЙЛАМИ 


#записать в файл json

import json  # noqa: E402, F401

data = {"nameeeeeeeee" : "Mike", "age" : 30, "city" : "New York"}

#открываем файл
file = open("files/data.json", "w") #w -писать


json.dump(data, file, indent=4) #этот метод записывает информацию в файл, indent = отступы


#закрыть файл ! ОБЯЗАТЕЛЬНО 

file.close()


#ЧТОБ ВСЕ РАБОТАЛО И ФАЙЛЫ СОЗДАВАЛИСЬ/ОТКРЫВАЛИСЬ/ЗАКРЫВАЛИСЬ И Т.П. - НУЖН РАБОТАТЬ ИМЕННО В ТОЙ ДИРЕКТОРИИ В ТЕРМИНАЛЕ

#------------------
#прочитать файл

#1) открываем файл

file = open("files/data.json", "r") #r -читать

loaded_data = json.load(file)  #метод лоад - для чтения
file.close()
print(loaded_data)


#--------------------------------------------
#FILE CSV - это построчный набор данных, разделенный сепаратором - чаще всего запятой
import csv  # noqa: E402, F401 ИМПОРТИРУЕМ БИБЛИОТЕКУ CSV

rows = [['name', 'age', 'occupation'],  #заголовки
        ['John', 28, 'Engineer'],       #далее столбцы
        ['Marie', 22, 'Designer'],
        ['Mike', 32, 'Doctor'],
        ['Jack', 26, 'Artist'],
        ['Emma', 32, 'Programmerrrr']]

file = open("files/persons.csv", "w") #открываем файл и открываем его на запись 

csv_writer = csv.writer(file)

csv_writer.writerows(rows)

file.close 
#прочитаем файл 
file = open("files/persons.csv", "r") 

csv_dict_reader = csv.DictReader(file)

for row in csv_dict_reader:
    print(row["name"], row["age"], row["occupation"])

file.close()

#--------------------------------------------------------------------------------------------
