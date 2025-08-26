#функция это блок кода лля многократного повторения, отдельяется от остального кода двумя строками



#пример написания функции (подсчет кол-ва гласнх в строке)

def count_vowels(string):
    VOWELS = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in VOWELS:
            count += 1

    
    return count

print(count_vowels("Hello, world!"))
print(count_vowels("Python is a very powerful language."))
#-----------------------------------------------------------
#заглушка 

def nothing():
    # print("this function does nothing")
    pass                      #чтоб функция ничего не делала 

nothing() #синтаксис функции без аргментов - пустые скобки 

#-----------------------------------------------------------

#у функции может быть больше одного аргумента 
def format_date(*, day: int, month: str) -> str:  # *- звездочка помогает становить, чтоб переменные без наименования не преедавались, -> это тип возвращаемого значения
    return f"The date is {day} of {month}"


print(format_date(month="October", day=15)) #даже можно местами поменять, все равно ключевые (именованные) аргументы напишутся в правильном порядке

#-----------------------------------------------------------

#в функции можно объявлять дефолтные аргументы - т.е. если при вызове функции аргумент для такого параметра не предоставлен, то используется значение по умолчанию.

def custom_greeting(*, name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"


print(custom_greeting(name="John", greeting="Good morning"))
print(custom_greeting(name="John"))

#-----------------------------------------------------------

#STEPIK 

#1 написать только определение функции

def keanu_reeves():
    print("YOU'RE BREATHTAKING")

#-----------------------------------------------------------

#2 Создайте функцию с именем say_hello_world , которая принимает на вход имя человека в виде строки и печатает фразу «{name} говорит hello world!»

def say_hello_world(name):
    print(f"{name} говорит hello world!")

print(say_hello_world('Jim Kerry'))

#-----------------------------------------------------------

#3 Напишите функцию summa_n, которая принимает одно целое положительное t число и находит сумму всех чисел от 1 до t включительно

def summa_n(t):
    S = 1
    for i in range(1, t+1):
        S += i
    print(f"Я знаю, что сумма чисел от 1 до {t} равна {S}")


print(summa_n(5))

#-----------------------------------------------------------

#4 Напишите функцию exponentiation, которая принимает на вход целое число и выводит на экран через пробел квадрат и куб этого числа. 

def exponentiation(x):
    # square = x**2
    # cube = x**3
    # print(square, cube)

    print(x**2, x**3)

print(exponentiation(5))

#-----------------------------------------------------------

#5 Напишите функцию sum_num для суммирования всех цифр строки

def sum_num(string: str) -> int:
    result = 0
    for symbol in string:
        # print(symbol)
        if symbol.isdigit():
            result += int(symbol)
    print(result)


print(sum_num("123QwertY321"))

#-----------------------------------------------------------


#6 Напишите функцию get_body_mass_index, которая принимает массу тела человека в кг и рост в см и рассчитывает индекс массы тела человека

def get_body_mass_index(mass,height):
    index = mass / (height /100)**2
    # print(index)
    # if index < 18.5:
    #     print("Недостаточная масса тела")
    # if 18.5 <= index <= 25:
    #     print("Норма")
    # if index > 25:
    #     print("Избыточная масса тела")
    print("Недостаточная масса тела" if index < 18.5 else "Норма" if 8.5 <= index <= 25 else "Избыточная масса тела")         #оказывается так тоже можно (?)

print(get_body_mass_index(90,180))

#-----------------------------------------------------------

#7 Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки

def check_password(password):
    symbol = "!@#$%*"   
    has_digit_count = 0             
    has_symbol = 0                  #0 и 1 == True и False 
    
    for char in password:     
        if char.isdigit():
            has_digit_count += 1
    
    for char in password:
        if char in symbol:
            has_symbol = 1

    if has_symbol and has_digit_count >= 3 and password.istitle() and len(password) >= 10:
        print("Perfect password")
    else:
        print("Easy peasy")

print(check_password("Qwerty17!5#$"))

#-----------------------------------------------------------

#8 count_letters, которая принимает на вход фразу и подсчитывает, какое количество в ней строчных(K) и заглавных (N) букв, все остальные символы игнорируются

def count_letters(phrase):
    N = 0
    K = 0
    for char in phrase:
        if char.isupper():
            N += 1
        if char.islower():
            K += 1

    print(f"Количество заглавных символов: {N}\nКоличество строчных символов: {K}")

print(count_letters("Привет, Старина"))

#-----------------------------------------------------------

import turtle  #с помощью этого модуля можно делать рисунки 

#функция помогает разбить большую задачу на маленькие и каждая функция решает свою определенную задачу
#все это можно засунуть в функцию 

def move(a):  #функция, которая делает движение вперед и угол 90 градусов
    turtle.forward(a)    #пиксели
    turtle.left(90)        #угол поворота и куда лево и ли право  

def drawSquare(a): #чтоб не повторять блок кода 4 раза вызываем просто функцию выше 4 раза
    for _ in range(4):
        move(a)


def drawSquareColor(a, color): #делаем цветной квадрат 
    turtle.color(color)  #указываем цвет, который передаем в вызове функции
    turtle.begin_fill() #начинает заполнение цветом
    #вместо шагов сразу передаем предыдущую функцию
    drawSquare(a) 
    # for step in range(4):
    #     move(a)
    turtle.end_fill()  #останавливает заполнение
    turtle.color('black')  #цвет линии 



turtle.speed(1)  #скорость отрисовки 

drawSquareColor(60, "red")
turtle.goto(150,150) #перемещение точки (координаты х и у), делаем квадрат в новой точке 
drawSquareColor(120, "blue")

#-----------------------------------------------------------

#ДЗ нарисовать прямоугольник 

import turtle 

def move(a):  #функция, которая делает движение вперед и угол 90 градусов
    turtle.forward(a)    #пиксели
    turtle.left(90)        #угол поворота и куда лево и ли право  

def mov(b):
    turtle.forward(b)    #пиксели
    turtle.left(90)        #угол поворота и куда лево и ли право 

def drawRectangle(a, b): #рисуем прямоугольник 
        move(a)
        mov(b)
        move(a)
        mov(b)


def drawRectangleColor(a,b,color):
    turtle.color(color)  #указываем цвет, который передаем в вызове функции
    turtle.begin_fill() #начинает заполнение цветом
    drawRectangle(a,b)
    turtle.end_fill()  #останавливает заполнение

turtle.speed(1)  #скорость отрисовки 

drawRectangleColor(120, 60, "yellow")

#-----------------------------------------------------------

#9 Функция repeat_please_n_times должна n раз распечатать фразу

def repeat_please_n_times(a):
    print("Just do it\n"*a)
    # print("Just do it" for _ in range(a))  или так
repeat_please_n_times(5)

#-----------------------------------------------------------

#10 Напишите функцию is_between, которая принимает три аргумента и печатает True, если первое число находится между двумя вторыми включительно

def is_between(a,b,c):  #параметры функции 
    if b <= a <= c or b >= a >= c:
        print(True)
    else:
        print(False)

is_between(5, 3, 6)  #агументы функции при ее вызове

is_between(5, 9, 1)

is_between(10, 2, 5)

#-----------------------------------------------------------

#11 Напишите функцию count_letter(text, letter), которая принимает два параметра

def count_letter(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    print(count)
    
print(count_letter('to be or not to be', 'b'))

#-----------------------------------------------------------

#12 Напишите функцию print_initials(name, surname, middlename), которая принимает три параметра: а затем выводит на печать фамилию и инициалы в определенном формате 

def print_initials(name, surname, middlename):
    print(f"{surname.title()} {name.title()[0]}.{middlename.title()[0]}.")

print_initials('Мария', 'Иванова', 'Филлиповна')

print_initials('евгЕний', 'петросян', 'ВаГАнович')


