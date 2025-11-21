import requests 
#HOMEWORK 

#  задание
#  1. Отправьте на https://api.binance.com/api/v3/ticker/price запрос БЕЗ аргумента params.
#  2. Изучите структуру ответа, сравните её с ответом в запросе без params.
#  3. Напишите код, который найдёт курс Etherium'а к доллару (ETHUSDT) в полученной из запроса структуре.




url = 'https://api.binance.com/api/v3/ticker/price'

response = requests.get(url)  #без params выдал все курсы валют 

content = response.content

# print(content)   
# print(type(content))  #байты


price_object = response.json()  #перегоняем в json 

# print(price_object)
# print(type(price_object))  #получился список словарей 

for dictionary in price_object:        #итерируемся по списку
    # for value in dictionary.values():  #итерируемся по словарю - НЕ НАДО 
    if dictionary["symbol"] == "ETHUSDT":   #если находим словарь с ключом символ == ETHUSDT
        print(dictionary["price"])          #печатаем его значение по ключу прайс 