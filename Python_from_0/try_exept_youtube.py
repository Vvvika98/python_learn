#функция, которая находит среднее значение 

def find_average(*, numbers:list) -> float:
    return sum(numbers) / len(numbers)


try:   #если эта строчка кода выполняется без ошибки, блок exept пропускается 
    print(find_average(numbers=[]))
except ZeroDivisionError: #перечисяем ошибки, которые могут случиться при испольнении этой функции 
    print("The list is empty")



#когда падает ошибка программа может ее перехватвать, для этого используется следующий синтаксис 


############# еще один кейс для примера #############

import requests 

try:
    url = 'https://api.binance.com/api/v3/ticker/price'

    response = requests.get(url, params={"symbol" : "BTCUSDT"})   #вызываем библиотеку с методом ГЕТ

    bitcoin_price = float(response.json()["price"])
    print(bitcoin_price)
except requests.exceptions.ConnectionError as error: #а если не будет интернета код упадет с ошибкой 
    print(f"Something goes wrong {error}") #прописали, что есть ошибка и указали какая именно

    


