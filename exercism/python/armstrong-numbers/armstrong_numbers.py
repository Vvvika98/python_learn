def is_armstrong_number(number):
    result = 0
    count = len(str(number))
    for num in str(number):
        result += int(num) ** count
    return number == result
    
    
    



print(is_armstrong_number(10)) #False

print(is_armstrong_number(153)) #True

print(is_armstrong_number(100)) #False

print(is_armstrong_number(9474)) #True