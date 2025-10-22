def square(number):        
    # if number not in (range(1,65)):
    #     raise ValueError("square must be between 1 and 64")  #если значение клетки вне допустимого диапазона        
    # if number == 1:
    #     return 1    #первое зерно на первой клетке
    # corn = 1        #первое зерно 
    # count = number - 1   #кол-во итераций т.е. кол-во клеток до данной клетки (заданное число минус 1)
    # for i in range(count):  #перебираем итерации
    #     corn *= 2     #зерно удваиваем

    # return corn

    if 0 < number < 65:
        return 2 ** (number-1)
    raise ValueError("square must be between 1 and 64")  #если значение клетки вне допустимого диапазона        
    

def total():
    # summary = 0    #сумма
    # for number in range(1,65):  #перебираем числа в интервале
    #     summary += square(number)   #сумма всех зерен на всех квадратиках = складываем значения из предыдущей функции
    # return summary

    return square(64) * 2 -1
    
print(square(10))
print(total())   

