if True:    
    print("Hello, world")

x = 10 
if x > 0:   
    print("x is positive")

# Иногда нужно ПРОВЕРИТЬ несколько условий

x = 6
if x > 0:   
    print("x is positive")

elif x < 0: 
    print("x is negative")

else:   
    print("x is zero")


# если условия наслаиваются - исполняется ТО, которое ВЫШЕ


# если нужно проверить ДВЕ переменные на условия 

x = 10
y = 20 
if x > 0:   
    if y > 0:   
        print("x and y are positive")
# так не совсем корректно 

# лучше так 
x = 10
y = 20 
if x > 0 and y > 0:   
        print("x and y are positive")


# проверка с текстовыми переменными 
message = "Hello, world"
if message:     
    print("meesage is not empty")


# функция определения високосного года
year = 2004

if year % 4 == 0 and year % 100 != 0:   
    print("yaer is leap")
elif year % 400 == 0:   
    print("yaer is leap")
else:
    print("yaer is not leap")

# второй вариант 
year = 2004

if not year % 4 and year % 100:   
    print("yaer is leap")
elif year % 400:   
    print("yaer is leap")
else:
    print("yaer is not leap")
