# ЗАДАНИЕ: определить кол-во букв "о" в строке, а также их индексы

greeting = "Hello, world!"

# создаем лист, где будут храниться индексы наших букв О и переменную каунт для отсчета 
indexes = []
count = 0

# создаем цикл 

for i in range(len(greeting)):
    if greeting [i] == "o":
         # если переменная гритинг, т.е. буква с этим идексом будет равно "о"
        count += 1
        indexes.append(i)

print(count)
print(indexes) 