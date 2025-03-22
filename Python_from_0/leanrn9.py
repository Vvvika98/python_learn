file_names = ["document.txt" , "imaje.jpg" , "document2.txt" , "image2.jpg"]

# вывести имена в терминал
for file_name in file_names:
    print(file_name)


# цикл for можно использовать со строками
greeting = "Hello, world!"
for char in greeting:
    print(char)


# сосчитаем кол-во букв "O" в строке
greeting = "Hello, world!"
count_o = 0
for char in greeting:
    if char == "o":
        count_o = count_o + 1
        print(char)
print(count_o) 

# данная конструкция не удобна, для упрощения частотных задач используется СИНТАКСИЧЕСКИЙ САХАР 
reeting = "Hello, world!"
count_o = 0
for char in greeting:
    if char == "o":
        count_o += 1
print(count_o) 


#  циклы могут быть вложенными друг в друга 
students = ["Alice", "Bob", "Charlie", "David"]
for student in students:
# верхнеуровневый цикл - выведет все имена 
    print(student)
# внутренний цикл - выдать каждый символ 
    for char in student:
        print(char)
# пример как исполняется программа в рамках двух циклов 

# Вложенность для циклов опасная вещь: максимум один вложенный цикл и далее программу нужно дробить. 


#вместе с циклами используется ДВА КЛЮЧЕВЫХ СЛОВА: continue , beak 


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# если число не четное - выводим в терминал, если нет - ничего не делаем 
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
# если число не четное выполняется три шага и как раз используется функция print


# числа > 10 н выводим на экран, <10 = print 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in numbers:
    if num == 10:
        break 
    print(num)

# генерация последовательности чисел 
range_object = range(10)
print(range_object)

numbers = list(range_object)
print(numbers)
# получился список (лист) из рендж обджекта 
# как и в слайсах - это полуоткрытый интервал, последнее значение не входит в совокупность элементов 


# можно и начать с определенно числа 
my_range = range(1, 11)
print(list(my_range))


# можно добавить шаг
my_range = range(1, 11, 2)
print(list(my_range))
# вошло каждое второе число


# последовательность может быть убывающей 
my_range = range(10, 1, -1)
print(list(my_range))


# к последовательности чисел прибавить единичку 
numbers = [10, 11, 12, 13, 14, 15]

for number in numbers:
    number += 1
print(numbers)
# таким образом ничего не поменяется, т.к. intовая переменная не может меняться в Питоне
# для этого нам нужно поменять каждый элемент по идексу (на список)

numbers = [10, 11, 12, 13, 14, 15]
for i in range(len(numbers)):
    print(i)
# i - переменная индекс
# запринтить индексы нашего массива

numbers = [10, 11, 12, 13, 14, 15]
for i in range(len(numbers)):
    numbers[i] += 1
    print(numbers)
# изменили на единицу значение каждого элемента 
