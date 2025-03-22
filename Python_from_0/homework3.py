# ЗАДАНИЕ
# Сделайте таблицу умножения. Построчно выведите в консоль примеры:
# 1 * 1 = 1
# 1 * 2 = 2
# ...
# 9 * 9 = 81

# решение 
numbers = range(1, 10)
numbers2 = range(1, 10)
for num in numbers:
    # print(num)
    for num2 in numbers2:
        # print(num, num2)
        result = num * num2 
        # print(result)
        print(f"{num} * {num2} = {result}") # 

