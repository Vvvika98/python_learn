"""
Задание: Пользователь вводит строковое значение, мы приводим его к числовому и, если оно не приводится к числовому - 
мы пользователю должны сказать, что данное значение не является цифрами
"""

my_string = input("Enter a number: ")
if my_string.isdigit():   
    my_integer = int(my_string)

else:   
    print(f"{my_string} is not a number")
