def is_armstrong_number(number):
    result = 0
    num = str(number)
    count = len(num)
    for n in num:
        result += int(n) ** count
    return number == result
    
    
    
#переписать без использования строки


print(is_armstrong_number(10)) #False

print(is_armstrong_number(153)) #True

print(is_armstrong_number(100)) #False

print(is_armstrong_number(9474)) #True