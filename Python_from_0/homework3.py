# ЗАДАНИЕ
# Сделайте таблицу умножения. Построчно выведите в консоль примеры:
# 1 * 1 = 1
# 1 * 2 = 2
# ...
# 9 * 9 = 81

# решение 
numbers = range(1, 10) #создаем переменную 1 с последовательностью чисел 
numbers2 = range(1, 10) #создаем переменную 2 с последовательностью чисел 
for num in numbers: # цикл 1
    # print(num)
    for num2 in numbers2: # цикл 2
        # print(num, num2)
        result = num * num2 
        # print(result)
        print(f"{num} * {num2} = {result}") # в ф-строку можно вписывать любые значения, а переменные брать в {}

