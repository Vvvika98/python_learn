def square(number):        
    if number not in (range(1,65)):
        raise ValueError("square must be between 1 and 64")  #если значение клетки вне допустимого диапазона        
    if number == 1:
        return 1    #первое зерно на первой клетке
    corn = 1        #первое зерно 
    count = number - 1
    for i in range(count):
        corn *= 2

    return corn

def total():
    summary = 0
    for number in range(1,65):
        summary += square(number)
    return summary


print(square(10))
print(total())   

