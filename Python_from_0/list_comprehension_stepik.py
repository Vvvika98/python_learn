#1 При помощи генератора-списка создайте список, состоящие из N нулей, и выведите его в качестве ответа

n = int(input())
result = [0 for num in range(n)]
print(result)

#2 При помощи генератора-списка создайте список [1, 2, 3, ..., n], само натуральное число n будет поступать на вход вашей программе

n = int(input())
result = [i for i in range(1, n+1)]
print(result)

#3 при помощи генератора списков создайте новый список, в котором каждый элемент создается по шаблону

names = ['Alice', 'Bob', 'Marry', 'Joe', 'Hilary', 'Stevia', 'Dylan', 'Kevin', 'Darvin']

result = [f'My name is {name}' for name in names]
print(result)

#4 Перепишите программу ниже при помощи генератора списков
#было
n = int(input())          #подается на ввод число           

result = []               #пустой список              
for x in range(n + 1):    #цикл до числа n включительно    
    if x % 2 == 0:        #если число без остатка делится на 2 (четное)   
        result.append(x * x)  #добавляем в конец пустого списка квадрат этого числа 
print(result)

#стало 
n = int(input())    
result = [x*x for x in range(n+1) if x % 2 == 0]
print(result)


#5 создайте список, состоящий из делителей введенного числа

n = int(input()) 

result = [num for num in range(1, n+1) if n % num == 0]   #число n делится без остатка на num, именно эти num и остаются
print(result)

#6 создайте список, состоящий из нечетных натуральных чисел в интервале [ n; n2 ]

n = int(input())  
result = [num for num in range(n, (n**2)+1) if num % 2 != 0]
print(result)

#7 Если a ≤ b, необходимо сформировать список квадратов, Если a > b, необходимо сформировать список кубов

a, b = map(int, input().split())
if a <= b:
    result = [num**2 for num in range(a, b+1) ]
if a>b:
    result = [num**3 for num in range(b, a+1)]
    result.reverse()
print(result)

#8 Создайте список первых букв каждого слова строки, хранящейся в переменной phrase

phrase = 'Create a list of the first letters of every word in this string' 

result = [i[0] for i in phrase.split()]   #применили метод к строке прям в ЛК

print(result)

#9 Создайте список, состоящий из первых n заглавных букв английского алфавита
from string import ascii_uppercase                   #импортируем альфавит 
# print(ascii_uppercase)

n = int(input()) 


result = [letter for letter in ascii_uppercase[0:n]]  #срезом 
print(result)   

#10 вывести список, состоящий из первых n заглавных букв английского алфавита, где каждая буква повторяется количество раз, соответствующее её порядковому номеру
from string import ascii_uppercase                   #импортируем альфавит 
# print(ascii_uppercase)


n = int(input()) 


result = [letter*(i+1) for i, letter in enumerate(ascii_uppercase[:n])]  #энумирейт возвращает последовательность кортежей i - 0,1,2... letter - A,B,C...
print(result)         

#11 Генератора списков создайте список слов, которые начинаются с буквы «t» или «T»

phrase = 'Take only the words that start with t in this sentence'

result = [i for i in phrase.split() if 't' in i[0] or 'T' in i[0]]
print(result)


