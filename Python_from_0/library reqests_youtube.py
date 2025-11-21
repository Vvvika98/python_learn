import requests 

url = 'https://api.binance.com/api/v3/ticker/price'

response = requests.get(url, params={"symbol" : "BTCUSDT"})   #вызываем библиотеку с методом ГЕТ


content = response.content

print(content)   #курс биткоина к доллару b'{"symbol":"BTCUSDT","price":"113650.21000000"}'
print(type(content))


#перегоняем в json 

price_object = response.json()


price = float(price_object["price"])   #в переменную присваиваем значение ключа ПРАЙС и делаем флоат, т.к. до этого это было строкой

print(price)

#----------------------------------------------------------------------------

#делаем код, который каждую секунду ходит к АПИ бинанса и узнает курс битка 

import time  # noqa: E402 модуль стандартной бибилиотеки 

bitcoin_prices = []
for i in range(30):    #итерируемся на 30 секунд
    response = requests.get(url, params={"symbol" : "BTCUSDT"})  #вызываем библиотеку с методом ГЕТ курс битка к доллару
    price = float(response.json()["price"])    #перегоняем в json, в переменную присваиваем значение ключа ПРАЙС и делаем флоат, т.к. до этого это было строкой
    bitcoin_prices.append(price)           #добавляем значения битка в пустой список
    time.sleep(1)       #замираем на 1 секунду 

print(bitcoin_prices)
print(len(bitcoin_prices))
print(max(bitcoin_prices))
print(min(bitcoin_prices))


#----------------------------------------------------------------------------

