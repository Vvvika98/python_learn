# Homework
# 1) метод строк format()
my_string = 'Hello, {}!'.format("Vasya")
print(my_string)


my_string = "{0} , {1} , {2}".format('a' , 'b' , "c")
print(my_string)




my_string = "{} , {} , {}".format("a" , "b" , "c")
print(my_string)
# вопрос: для чего цифры тогда? Если можно и без них


my_string = "{2} , {0} , {1}".format('a' , 'b' , "c")
print(my_string)
# типа он по умолчанию знает что 0 - а, 1- в, 2 - с?


my_string = "{0} , {1} , {2}".format(*"abc")
print(my_string)

my_string = "{0}{1}{0}".format("mama" , "dady")
print(my_string)


values = ["Charlie" , 35]
massage = "Name {0} , age {1}".format(values[0] , values [1])
print(massage)
# постановка по индексу 

# постановка по имени
name = "Alice"
age = 30
massage = "Name {} , age {}".format(name, age)
print(massage)


# постановка по ключевым словам
massage = "Name: {name}, age: {age}".format(name="Bob" , age="12")
print(massage)


pi = 3.14159
formatted_pi = "Значение pi: {:.2f}".format(pi)  # Округление до 2 знаков после запятой
print(formatted_pi)  # Вывод: Значение pi: 3.14

number = 12345
formatted_number = "Число: {:,}".format(number)  # Разделитель тысяч
print(formatted_number)  # Вывод: Число: 12,345

percentage = 0.85
formatted_percentage = "Процент: {:.1%}".format(percentage)  # Отображение в процентах
print(formatted_percentage)  # Вывод: Процент: 85.0%



number = 42
padded_number = "{:04}".format(number)  # Заполнение нулями до 4 символов
print(padded_number)  # Вывод: 0042

text = "World"
filled_text = "{:*^10}".format(text)  # Заполнение звездочками до 10 символов, выравнивание по центру
print(filled_text)  # Вывод: **World***





# 2) метод процентного форматирования 
"""
string % (значения)

 string: Строка, содержащая заполнители формата (например, "Привет, %s!").
•  %: Оператор, выполняющий подстановку.
•  (значения): Кортеж (или иногда одно значение, если у вас только один заполнитель), содержащий значения, которые вы хотите вставить в строку.

Заполнители

Заполнители сообщают Python, как форматировать значения. Вот некоторые распространенные:

•  %s: Строка (любой объект, который можно представить в виде строки).
•  %d или %i: Целое число.
•  %f: Число с плавающей точкой.
•  %x или %X: Шестнадцатеричное целое число (в нижнем или верхнем регистре).
•  %o: Восьмеричное целое число.
•  %e или %E: Число с плавающей точкой в экспоненциальной (научной) нотации.
•  %%: Буквальный знак процента (%).
"""
name = "Алиса"
age = 30
price = 19.99

# Простое добавление строки
greeting = "Привет, %s!" % name
print(greeting)  # Вывод: Привет, Алиса!

# Вставка нескольких значений
message = "Меня зовут %s и мне %d лет." % (name, age)
print(message)  # Вывод: Меня зовут Алиса и мне 30 лет.

# Форматирование числа с плавающей точкой
price_string = "Цена: %.2f" % price  # Два знака после запятой
print(price_string)  # Вывод: Цена: 19.99

# Форматирование целого числа в шестнадцатеричном формате
hex_value = "Шестнадцатеричное значение 255: %x" % 255
print(hex_value)  # Вывод: Шестнадцатеричное значение 255: ff

# Использование знака процента
percentage = "Скидка: %d%%" % 10
print(percentage)  # Вывод: Скидка: 10%

"""
Вы можете добавлять модификаторы ширины поля и точности к заполнителям:

•  %[ширина][.точность]код_формата

•  ширина: Минимальная ширина поля. Если значение короче ширины, оно будет дополнено (обычно пробелами). Если значение длиннее, оно будет отображено без усечения.
•  .точность: Для чисел с плавающей точкой (%f, %e) это определяет количество цифр после десятичной точки. Для строк (%s) это определяет максимальное количество символов для включения.
•  код_формата: Тип заполнителя (s, d, f и т. д.).
"""

# Пример ширины и точности
number = 123.4567

formatted_number = "Число: %10.2f" % number  # Ширина 10, 2 знака после запятой
print(formatted_number)  # Вывод: Число:     123.46 (дополнено пробелами)

short_string = "Короткая строка: %.3s" % "Это длинная строка" # Макс. 3 символа
print(short_string) # Вывод: Короткая строка: Эт

data = {"name": "Боб", "age": 40}
info = "Имя: %(name)s, Возраст: %(age)d" % data
print(info)  # Вывод: Имя: Боб, Возраст: 40

