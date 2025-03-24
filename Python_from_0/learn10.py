# есть лист  и надо высчитать среднее значение списка
numbers_1 = [1, 2, 3, 4, 5]

average_1 = sum(numbers_1) / len(numbers_1) #average - среднее
print(average_1)

# две последовательности, у которых надо высчитать среднее значение 
numbers_2 = [6, 7, 8, 9, 10]
average_2 = sum(numbers_2) / len(numbers_2)
print(average_2)

# написано плохо, потому что нарушен принцип DRY

# чтобы этого избежать необходимо использовать функции 
numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]


#у функции должно быть осознанное название 
def find_average(numbers):
    average = sum(numbers) / len(numbers)
    return average


average_1 = find_average(numbers_1)
average_2 = find_average(numbers_2)
print(average_1, average_2) #принтить можно несколько результатов сразу



# функция для подсчета гласных в строке


def count_vowels(string):
    VOWELS = "aeiouAEIOU" #в пайтон все решистрозависимое, поэтому А и а - это разные буквы
    count = 0 #переменная для подсчета 
    for char in string:
        if char in VOWELS:
            count += 1 #применили синтаксический сахар 
    return count


print(count_vowels("Hello, world!"))
print(count_vowels("Python is a very powerful language."))


# надо сделать "заглушку" чтоб функция ничего не исполняла


def nothing():
    print("this fuction does nothing") #перевод: эта функция ничего не делает 


nothing() #вызов функции 

# чтобы функци ничего не делала передаем ключевое слово "pass"


def nothing():
    pass
# блок кода не будет исполняться 

# у функций может быть больше одного аргумента 


def formate_date(*, day: int, month: str) -> str:  # передать типы переменных int и str | * - означает, что без date, month она не вызовется | -> тип возвращаемого значения
    return f"The date is {day} of {month}" #передаем f-строку 


print(formate_date(day=15, month="October")) #данные могут перепутать, поэтому стоит уточнять типы данных и возвращаемых значений 


