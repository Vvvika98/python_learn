#0 КЕЙС НА ОБУЧЕНИИ 
s = "IVANOV IVAN Samara SGU 5 4 5 5 4 3 5" #СОЗДАЕМ СПИСОК В КОТОРОМ ЕСТЬ ДАННЫЕ О ЧЕЛОВЕКЕ
person = {} #создаем пустой словарь, что его заполнить значениями выше  

s = s.split() #разбиваем строку по пробелам, образовывая список 
# print(s) 

#создаем ключи двигаясь по индексам образованного списка 
person["lastName"] = s[0]
person["firsName"] = s[1]
person["sity"] = s[2]
person["university"] = s[2]
person["marks"] = [] #пока пустой список, потому что оценки ледат в списке как отдельные строки

#создает цикл фор для того, чтобы применить метод и собрать оценки с один список
for mark in s[4:]: #для оценок из списка ЭС
    person["marks"].append(int(mark)) 
    #в наш пустой список в ключ "оценки" добавлять эти строки с оценками используя метод, но т.к. это строки, а нам надо добавлять целые числа добавляем функцию ИНТ
print(person)



#1 СОЗДАТЬ ПУСТОЙ СЛОВАРЬ
my_dict = {}

print(my_dict)

#2 создайте словарь, у которого должны быть следующие пары ключ-значения

person = {
    'name': 'Vasya',
    'surname': 'Petrov',
    'age': '25'
}

print(person)

#3 В отдельных строках распечатайте сперва значение ключа name, потом calories и напоследок id
sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}

print(sweet["name"])
print(sweet["calories"])
print(sweet["id"])

#4 Ваша задача — по введеному номеру месяца вывести количество дней.
days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

day = int(input())

print(days[day])

#5 МОЖНО ПРИБАВЛЯТЬ К ЗНАЧЕНИЯМ ТЕМ САМЫМ ИЗМЕНЯЯ ИХ
man = {"name": "John", "age": 30}
man['car'] = 'Bentley' #ДОБАВИЛИ НОВУЮ ПАРУ КЛЮЧ-ЗНАЧЕНИЕ
man['age'] += 1 #ПРИБАВИЛИ БУДЕТ 31
man['name'] = 'Sir John' #ИЗМЕНИЛИ ЗНАЧЕНИЕ ПЕРВОГО КЛЮЧА 
print(man)


#6 Создать два новых ключа, изменить два значения уже существующих ключей, выдать готовый ответ
sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}

sweet["weight"] = 230
sweet["have_topping"] = True 
sweet["name"] = "SuperCake"
sweet["calories"] = 350
print(sweet)

#7 Удалить ключи - ppu, type, вывести итог на экран
sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}

del sweet["ppu"], sweet["type"] #можно в одну строчку 
print(sweet)

#8 Вам необходимо создать словарь, который будет включать в себя ключи от 1 до n, а значениями соответствующего ключа будет значение ключа в квадрате
n = int(input())               #создаем инпут - наш квардрат чисел

d = {}                         #создаем пустой словарь 

for key in range(1, n+1):      #с помощщью цикла обходим числа от 1 до n
    d[key] = key*key #с помощью метода создаем ключи к словарям, в качестве второго значения вместо None можно передать значение - т..е наш квардрат числа
print(d)                       #выводим полученный словарь 


#9 словарь alphabet, где ключи  - строчные английские символы, а значения - порядковые номера букв в алфавите начиная с 1.
from string import ascii_lowercase                     #импорт всех строчных букв английского алфавита
# print(ascii_lowercase)


# letters = list(ascii_lowercase)                      #создаем список с буквами НЕ НАДО 
# print(letters)

alphabet = {}                                           #создаем пустой словарь

for i, key in enumerate(ascii_lowercase, start=1):     #создаем цикл фор итерируя по строке алфавита ENUMIRATE ДОБАВЛЯЕТ СЧЕСТЧИК К КАЖДОМУ СИМВОЛУ НАЧИНАЯ С 1
    alphabet[key] = i                         #с помощуью метода словаря добавляем пару ключ=значеине в наш пустой словарь
print(alphabet) 


#10 Удаление букв из словаря 


alphabet = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
    'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
    'w': 23, 'x': 24, 'y': 25, 'z': 26
}

deleted_letters = list(input()) #список строк, которые представляют собой ключи, которые мы хотим удалить из словаря 


# deleted_letters = "q w e r t y u i o p a s d f g h j k l z x c"             
# deleted_letters = list(deleted_letters.replace(' ', ''))   #список строк, которые представляют собой ключи, которые мы хотим удалить из словаря 
# print(deleted_letters)

#ПОПЫТКА 1 for key in alphabet:
#     print(key, alphabet[key])
    # if key in deleted_letters:
    #     del alphabet[key]
    #     # alphabet.pop(key)
# # print(key)

#ПОПЫТКА 2 if deleted_letters in alphabet:
#     alphabet.pop(len(deleted_letters))
#     print(alphabet)
    
#ВЕРНАЯ ПОПТЫКА 3
#безапасное удаление ключей! терируем по списку ключей, которые нужно удалить, а не по ключам самого словаря.
for key in deleted_letters:  #с помощью цикла переменной КЕЙ присваиваетя значение одного из элементов ДЕЛЕТЕД ЛЕТЕРС
    # print(key)
    if key in alphabet:      #создаем условие, что если КЕЙ входит в словарь, удали эти клбчи из словаря
        del alphabet[key]
print(alphabet)              #выводим на экран обновленный словарь 


#ВЕРНЯ ПОПЫТКА 4 
for k in deleted_letters:    #итеририруем по списку ключей, кот. нужно удалить (создавая "копию ключей")
    alphabet.pop(k, None)    #с помощью метода удаляем ключи из словаря 
print(alphabet)

#11 Определение самого «дорогого» слова!

alphabet = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
    'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
    'w': 23, 'x': 24, 'y': 25, 'z': 26
}

words = (input().split())                 #разделяем на три слова и оборачиваем в список
# print(words)                            #проверка 


sum_words = {}                            #создаем пустой словарь где сохраним ключ-значение (слово: его сумма)


for word in words:                        #перебираем слова из исходной строки
    word_sum = 0                          #сумма для текущего слова (сбрасываем на 0 для каждого нового слова)
   #print(word)                           #проверка 
    for char in word:                     #перебираем символы из каждого слова
    # print(char)                         #проверка 
        if char in alphabet:              #если символ в словаре
            word_sum += alphabet[char]    #в пустую переменную для отсчета с помощью метода получаем сумму символов каждого слова "GET"-безопасное извлечение значения по заданному ключу
        # print(alphabet.get(char))       #проверка 
    sum_words[word] = word_sum            #добавляем в пустой словарь(слово = его сумма)
#print(result)                            #проверка  

# heavy_word = max(sum_words, key=sum_words.get)  #самое тяжелое слово - метод GET ВОЗВРАЩАЕТ ЗНАЧЕНИЕ КЛЮЧА. Функция max вызывает метод ГЕТ для каждого аргумента (передаем его через key)
# print(heavy_word)
max_key = ""
max_value = 0

for key, value in sum_words.items():      #определение максимального значения 
    if value >= max_value:
        max_key = key
        max_value = value
print(max_key)
    



#ЧАСТЬ 2 
#НЕЛЬЗЯ ОБРАЩАТЬСЯ К НЕСУЩЕСТВУЮЩИМ КЛЮЧАМ В СЛОВАРЕ - ВЫДАТСЬ ОШИБКУ КЕЙЭРРОР
digits = {1: 'one', 2: 'two', 3: 'three'}

key = 4
if key in digits:
    print(f"Ключ {key} есть в словаре, его значение: {digits[key]}")
else:
    print(f"Ключ {key} отсутствует в словаре")


#1 вычисляем длину словаря 
account = {
  "id": 5681,
  "uid": "45f17b56-bcad-4933-8c73-a37aaa6863b9",
  "account_number": "6733198878",
  "iban": "GB79PNXF20678598570754",
  "bank_name": "AAC CAPITAL PARTNERS LIMITED",
  "routing_number": "007398728",
  "swift_bic": "AACCGB21"
}

print(len(account))

#ДОБАВИТЬ ЭЛЕМЕНТ В СЛОВАРЬ 
inventory = {'apples': 10, 'oranges': 5}
if 'bananas' not in inventory:
    inventory['bananas'] = 7
print(inventory)

#ИЗМЕНИТЬ ЗНАЧЕНИЕ В СЛОВАРЕ 

inventory = {'apples': 10, 'oranges': 5}
if 'oranges' in inventory:
    inventory['oranges'] += 7
print(inventory)

#2 Проверить есть за заданные ключи в словаре 
address = {
    "zip_code": "123456",
    "longitude": 45.6789,
    "post_code": "654321",
    "street_name": "Main Street",
    "number_house": 10
}

address = {
    "zip_code": "789012",
    "longitude": 50.1234,
    "street_name": "Broadway"
}

print("zip_code" in address)
print("longitude" in address)
print("post_code" in address)
print("street_name" in address)
print("number_house" in address)

#3 ПЕРЕДАТЬ КУРС ВАЛЮТЫ В СЛОВАРЕ
currencies = {
    'Argentine Peso': 118362.205708,
    'Australian Dollar': 1586.232315,
    'Bahraini Dinar': 423.780164,
    'Botswana Pula': 13168.450636,
    'Brazilian Real': 5954.781483,
    'British Pound': 834.954104,
    'Bruneian Dollar': 1520.451015,
    'Bulgarian Lev': 1955.83,
    'Canadian Dollar': 1430.54405,
    'Chilean Peso': 898463.818465,
    'Chinese Yuan Renminbi': 7171.445692,
    'Colombian Peso': 4447741.922165,
    'Croatian Kuna': 7527.744707,
    'Czech Koruna': 24313.797041,
    'Danish Krone': 7440.613895,
    'Emirati Dirham': 4139.182587,
    'Hong Kong Dollar': 8786.255952,
    'Hungarian Forint': 355958.035747,
    'Icelandic Krona': 143603.932438,
    'Indian Rupee': 84241.767127,
    'Indonesian Rupiah': 16187150.010697,
    'Iranian Rial': 47534006.535121,
    'Israeli Shekel': 3569.191411,
    'Japanese Yen': 129149.364679,
    'Kazakhstani Tenge': 489292.515538,
    'Kuwaiti Dinar': 340.959682,
    'Libyan Dinar': 5196.539901,
    'Malaysian Ringgit': 4717.485104,
    'Mauritian Rupee': 49212.933037,
    'Mexican Peso': 23130.471272,
    'Nepalese Rupee': 134850.008728,
    'New Zealand Dollar': 1703.649473,
    'Norwegian Krone': 9953.078431,
    'Omani Rial': 433.360301,
    'Pakistani Rupee': 198900.635421,
    'Philippine Peso': 57574.278782,
    'Polish Zloty': 4579.273862,
    'Qatari Riyal': 4102.552652,
    'Romanian New Leu': 4946.638369,
    'Russian Ruble': 86197.012666,
    'Saudi Arabian Riyal': 4226.530892,
    'Singapore Dollar': 1520.451015,
    'South African Rand': 17159.831129,
    'South Korean Won': 1355490.097163,
    'Sri Lankan Rupee': 228245.645722,
    'Swedish Krona': 10439.125427,
    'Swiss Franc': 1037.792217,
    'Taiwan New Dollar': 31334.286611,
    'Thai Baht': 37436.518169,
    'Trinidadian Dollar': 7636.35428,
    'Turkish Lira': 15078.75981,
    'US Dollar': 1127.074905,
    'Venezuelan Bolivar': 511082584.868731
}

currency = str(input())

if currency in currencies:
    print(currencies.get(currency))
else:
    print(f"Нет данных по {currency}")

#4 ВЫВЕСТИ НА ЭКРАН ВСЕ КЛЮЧИ СЛОВАРЯ В КАЧЕСТВЕ КОРТЕЖА
account = {
  "id": 3136,
  "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
  "account_number": "0847799459",
  "iban": "GB90XTND56373623909314",
  "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
  "routing_number": "126602476",
  "swift_bic": "BCYPGB2LHGB"
}

print(tuple(account.keys))

#5 СЛИЯНИЕ КЛЮЧЕЙ (ЭТО БЫЛО piЗДЕЦ КАК ЛЕГКО, НО НЕ ДОГАДАЛАСЬ)
d1 = {"Brazil": "Brasilia", "Argentina": "Buenos Aires", "Peru": "Lima"}     
d2 = {"Argentina": "Córdoba", "Chile": "Santiago", "Peru": "Cusco"} 

# for value1 in d1:
#     print(d1[value1])
# for value2 in d2:
#     print(d2[value2])

# for key1 in d1:
#     print(key1)
# for key2 in d2:
#     print(key2)

# if key1 == key2:
#     d2.setdefault(key1, value1)
#     print(d2)

result = d1 | d2 | d1
print(result)


#6 слово (строку из английских букв) и вычисляет сумму соответствующих числовых значений букв из словаря
alphabet = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
    'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
    'w': 23, 'x': 24, 'y': 25, 'z': 26
}

word = str(input())

result = 0
for key in word:                  #перебираем ключи в новой переменной 
  # print(key)                    #проверка 
  if key in alphabet:             #если ключ в словаре
    result += alphabet.get(key)   #в пустую переменную для осчета с помощью метода получаем значение и сладываем с каждым циклом 
    # print(alphabet.get(key))
print(result)                     #итоговый результат сложение всех ключей слова 




#7

#МЕТОДЫ СЛОВАРЯ 
#Необходимо подсчитать, сколько раз каждое слово встречается в списке. Решение с использованием метода .setdefault():

word_count = {}
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

for word in words:
    word_count.setdefault(word, 0)
    word_count[word] += 1

print(word_count)  # {'apple': 2, 'banana': 3, 'orange': 1}


#1 При данном методе уже имеющееся значение не меняется!!!! -1 ничего не дает 
inventory = {'apples': 10, 'oranges': 5, 'bananas': 7}
inventory.setdefault('oranges', -1)
print(inventory)


#2 Вмержить (соединить) словари 
d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}

d2.update(d1)  #нельзя сразу в принте сделать метод, т.к. сам метод меняет словарь "на месте" и вернет None
print(d2)


#3 Определить, к какой стране принадлежит введённый город

countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()



for key, item in countries.items():
  if city in item:
    print(f"INFO: {city} is a city in {key}")
    break
else:
  print(f"ERROR: Country for {city} not found")


""" break необходим для того, чтобы остановить цикл, как только город будет найден, и предотвратить выполнение блока else. Без break, 
else служит для обработки ситуации, когда цикл завершился, не найдя совпадений, а это не то, что нам нужно, если город уже был найден ранее. 

else выполняется только в том случае, если цикл for завершился "естественным" путем, то есть не был прерван оператором break.  
Это значит, что блок else будет выполнен только в том случае, если цикл полностью перебрал все страны в словаре countries, и ни в одной из них не был найден введенный город. """


#4 При помощи метода pop переименуйте в нем ключи


user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17"
}


user.pop("password")
user.pop("last_name")

user.setdefault("secret", "SyUpfo1ljm")
user.setdefault("surname","Wehner")

print(user)


#5 подсчитывает, сколько раз каждое число встречается в списке, и выводит результат в виде словаря
integers = (input().split())        #поступают на ввод числа - в данном случае строка, ЧИСЛА НЕ ЯВЛ. ИТЕРИРУЕМЫМ ОБЪЕКТОМ. Убираем пробелы

int_count = {}                      #создаем пустой словарь для подсчета того, сколько раз каждый символ (цифра) встречается в строке


for integer in integers:             #перебирает каждый элемент (каждую цифру в строке)
  number = int(integer)              #засунуть в переменную строчки и преобразовать в числа
  int_count.setdefault(number, 0)    #метод добавляет этот ключ в словарь и присваивает ему значение 0
  int_count[number] += 1             #увеличивает значение, связанное с ключом integer в словаре int_count, на 1


print(int_count)         



#СТРАННАЯ ЗАДАЧКА НА NONETYPE 
empty = None
empty_too = None 

if empty is empty_too:
    print(True)
if empty is not empty_too:
    print(False)
    
if empty == empty_too:
    print(False)
if empty != empty_too:
    print(True)

#ВТОРАЯ ЗАДАЧА NONETYPE 
i_love_none = [None]
i_love_none = i_love_none * 50

print(i_love_none)

#МЕТОДЫ СЛОВАРЯ, ИТЕРАЦИЯ СЛОВАРЕЙ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#1 найти ключ, связанный с максимальным значением, и вывести этот ключ на экран

letters = {"a": 10, "b": 20, "c": 25, "d": 15}

#ТАК РЕШИЛА КАКАЯ-ТО ЖЕНЩИНА, Я ТАК ПОКА ЧТО НЕ РЕШУ 
# max_key = max(letters, key=letters.get) #наход ключ с максимальным значением 
# print(max_key)



max_key = None
max_value = float('-inf')  # Инициализируем минимально возможным значением

for key, value in letters.items():
    if value > max_value:
        max_value = value
        max_key = key
print(max_key)


#2 нужно оставить только те книги, чьи идентификаторы состоят из количества символов, кратного трём
books = {
    'ASDFG': 320,
    'ZXC123': 250,
    'QWE': 110,
    'MNBVCXZ': 410,
    'LKH': 90
}

books_1 = books.copy()

for key in books.keys():
    if len(key) % 3 != 0:
        books_1.pop(key)
print(books_1)

#3 Необходимо создать "зеркальный" словарь

data = {'apple': 5, 'banana': 3, 'cherry': 5, 'date': 2}
result = {}

for key,value in data.items():          #итерируемся по ключам и значениям исходного словаря
    print(key,value)
    if value in result:                 #здесь было key и поэтому не получалось у меня 
        result[value].append(key)       #список строк (бывшие ключи - новые значения), поэтому метод применяем. print(result[value]) --- ['apple', 'cherry']
        result[value].sort()            #нужен метод для упорядочения списка (бывшие ключи - новые значения)
    else:
        result[value] = [key]           #меняем местами ключи и значения через присвоение 
print(result)

#второй вариант с применение сетдефолт 
result = {}
for key,value in data.items():
    result.setdefault(value,[])
    result[value].append(key)
for key in result:
    result[key].sort() 
print(result)

#4 нужно убрать из списка всех участников, кто набрал минимальное количество баллов

scores = {
    'Иванов': 15,
    'Петров': 20,
    'Сидоров': 15,
    'Кузнецов': 25
}

scores = {}
if len(scores) != 0:
    min_score = min(scores.values())                #находим минимальное значение 
# print(min_score)
min_keys = [key for key, value in scores.items() if value == min_score]
# print(min_keys)
for k in min_keys:
    if k in scores:
        del scores[k]
print(scores)

#5 Программа должна вывести на экран имя сотрудника с максимальным результатом
