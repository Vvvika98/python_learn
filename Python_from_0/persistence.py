from functools import reduce 

def persistence(n):
    numeric = [int(num) for num in str(n)]            #[9,9,9]
    count = 0   #кол-во умножений
    if n < 10:
        return 0  
    while len(numeric) > 1:
        multipl = reduce(lambda x, y: x * y, numeric)  #ПЕРВОЕ УМНОЖЕНИЕ 
        numeric = [int(x) for x in str(multipl)]
        count += 1

    return count 
    
# def prod_of_digits(n):
#     if n == 0:
#         return 0
#     prod = 1   #берем 1 за основу умножения, т.к. умножение на 0 даст 0!
#     while n > 0:   #пока число 
#         remainder = n % 10  #находим остаток от деления на 10 (последняя цифра)
#         if remainder == 0:  #если он равен 0
#             return 0        #возвращаем 0 
#         prod *= remainder   #1 * на остаток от деления
#         n //= 10            #число делится без остатка на 10 (отбрасываем последннюю цифру)
#     return prod             



# def persistence(n):
#     if 0 < n <= 9:    #если число однозначное 
#         return 0  #верни 0
#     count = 0     #шагов изначально 0 
#     while n >= 10: #пока число больше или равно 10
#         n = prod_of_digits(n)  #число = предыдущая функция от этого числа 
#         count += 1     #шаг +1
#     return count #верни кол-во шагов
            
        
#Цикл в persistence не прерывается, пока число не станет однозначным. 
#На каждой итерации этого цикла (которая увеличивает count на 1) 
# мы полностью вычисляем произведение цифр, используя prod_of_digits, 
# и заменяем старое многозначное число на это новое, меньшее произведение.

print(persistence(999))  #4

print(persistence(39))  #3

print(persistence(4))  #0



# def shuffle(nums: list[int], n: int) -> list[int]:
#     result = []
#     for i in range(0,n):
#         result.append(nums[i])  #0, 1
#         result.append(nums[n+i])  #2+0, 2+1
#     return result
    

# print(shuffle(nums=[3,5,8,1], n=2))   #[3, 8, 5, 1]