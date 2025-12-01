def steps(number):
    count = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return count
    while number != 1:
        number = number * 3 + 1 if number % 2 else number // 2 #тернарный оператор в цикле 
        count += 1
    return count 


# print(steps(1))  #0

# print(steps(3))  

# print(steps(1000000)) #152

# # print(steps(-15))   #ValueError