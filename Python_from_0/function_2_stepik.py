#7.3 RETURN 


#встроенные фукнции 
a = abs(-7)   #функция модуля числа 

b = max(4, abs(-90), 4, min(100,200))  #так тоже можно писать, функциию внутри функции, сначала действие происходит  скобках слево направо

#самописные функции 

def square(x):  #параметр функции 
    print(x**2)


a = square(6)   #аргумент, как раз запихнули его в переменную
print(a)        #получим NONE,  потому что не написали return, а по умолчанию return None


#-----------------------------------------------------------

#чтобы вернулось значение нужно написать:
def square_2(x):
    return x**2

a = square_2(square_2(9))   
print(a)  

# Слово RETURN в функции как BREAK в цикле 

#-----------------------------------------------------------
#напишем функцию, которая пишет ответ на вопрос четное ли число 

def even(x):
    # if x % 2 == 0:
    #     return True 
    # return False  
    return x%2==0         #вариант проще - при сравнении только два варианта True или False

for i in range(1,11):         #через цикл перебираем числа от 1 до 10
    print(i, even(i))         #вызываем функцию и само число


#-----------------------------------------------------------


# сочетание C(n,k) - 

#напишем фукнцию нахождения факториала

def factorial_1(x):
    pr =1 
    for i in range(2,x+1):
        pr = pr*i
    return pr

# for i in range(1,8):
#     print(i, factorial_1(i))

#напишем функцию сочетания 
def sochet(n,k):
    return factorial_1(n)/ (factorial_1(k)*factorial_1(n-k))


print(sochet(5,3))

#-----------------------------------------------------------

#функция нахождения площади и периметра 

def sqAndPer(a,b):
    mas = []
    mas.append(a*b)
    mas.append(2*(a+b)) 
    return mas              #результат будет список 
    # return a*b, 2*(a+b)   #результат будет кортежем 

#print(sqAndPer(3,6))
# square, perimetr = sqAndPer(2,5)
# print(square, perimetr)
print(sqAndPer(2,8))

#-----------------------------------------------------------

#1 Напишите функцию is_person_teenager , которая помогает по возрасту определить является ли человек подростком или нет.

def is_person_teenager(x):
    return 12 <= x <= 17

print(is_person_teenager(8))
print(is_person_teenager(15))

#-----------------------------------------------------------

#2 Напишите функцию factorial, которая принимает на вход одно неотрицательное число, и возвращает значение факториала данного числа.

def factorial(x):
    pr = 1 
    for i in range(2,x+1):
        pr *= i
    return pr


print(factorial(4))

#-----------------------------------------------------------

#3 Напишите функцию generate_fizz_buzz_list, которая принимает одно целое число n - размер списка

def generate_fizz_buzz_list(n):
    result = []
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0: 
            result.append("FizzBuzz")
        elif num % 3 == 0: 
            result.append("Fizz")
        elif num % 5 == 0: 
            result.append("Buzz")
        else: result.append(num)
    return result

print(generate_fizz_buzz_list(10))

#-----------------------------------------------------------

#4 В этой задаче вам необходимо воспользоваться уже готовой функцией gcd(a, b), которая принимает два числа и находит наибольший общий делитель для них.



#-----------------------------------------------------------

#5 Ваша задача написать функцию find_duplicate, которая принимает один аргумент - список чисел. Функция должна возвращать список из дублей, каждый дубль нужно брать только один раз в том порядке, в котором они встречаются в исходном списке. 

def find_duplicate(x):
    # result = []
    # for num in x:
    #     # print(num)
    #     if x.count(num) > 1:
    #         result.append(num)
    # return result 


    result = [num for num in x if x.count(num) >= 2]
    return list(dict.fromkeys(result))


        
print(find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]))
print(find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]))

#-----------------------------------------------------------

#6 Напишите функцию first_unique_char, которая принимает строку символов и возвращает целое число: позицию первого уникального символа в строке.
def first_unique_char(string):
    for char in string:
        # print(char)
        if string.count(char) == 1:
            return string.find(char)
    return -1


# print(first_unique_char("eret"))
# print(first_unique_char('abcabc'))
print(first_unique_char('abracadabra'))

#-----------------------------------------------------------