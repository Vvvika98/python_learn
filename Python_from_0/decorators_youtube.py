# декоратор - это синтаксический сахар, елает более быстрым написание каких-то частотных патернов 

#функция, как объявляется декоратор, самый простой 
def my_decorator(func):
    def wrapper(*args, **kwargs):                                                     #обертка переводится 
        print("Something is happening before the function is called.") #что случилось до вызова функции
        func(*args, **kwargs)                                                         #вызов функции
        print("Something is happening after the function is called.")  #что-то случилось после вызова функции
    
    return wrapper                                                     #возвращаем функцию враппер как объект


@my_decorator               #это эквиваленто
def say_hello(*, name: str) -> None:
    print(f"Hello, {name}!")

# my_decorator(say_hello)() #это эквивалентно 

say_hello(name="Sasha")     #вызываем функцию 

print("####################################")
#в данном примере функция ничего не возвращает

#--------------------------------------------------------------

#cделаем функцию, которая возвращает что-то

#переписываем декоратор 
def my_decorator(func):
    def wrapper(*args, **kwargs):                                                     #обертка переводится 
        print("Something is happening before the function is called.") #что случилось до вызова функции
        result = func(*args, **kwargs)  #присваиваем в переменную                                                    #вызов функции
        print("Something is happening after the function is called.")  #что-то случилось после вызова функции
        return result                  #возвращаем переменную
    return wrapper                                                     #возвращаем функцию враппер как объект

@my_decorator               
def add_numbers(*, a: int, b: int) -> int:
    print("Adding numbers...")
    return a + b

res = add_numbers(a=1, b=2)

print(res)

#--------------------------------------------------------------
#практика по декораторам 


import requests  # noqa: E402, F401
from requests.exceptions import RequestException #Поскольку это базовый класс, перехват RequestException позволяет перехватить любое исключение, связанное с requests.  Это упрощает обработку общих ошибок, связанных с запросами.  # noqa: E402
import time  # noqa: E402

#нужно сделать механизм ретраев - это когда он недоступен и ддо него через какое-то время нужно снова достучаться 


API_KEY = "BQGPUW9HYTACK9GUGMCWBNFE5" 

# def get_get_weather_by_hours_for_day_from_api(*, date: str, city: str) -> list[dict]:
#     url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}/{date}?unitGroup=us&key={API_KEY}"
#     respons = requests.get(url)

#     print(respons.json())

# date = "2023-08-04"
# city = "London, UK"
# get_get_weather_by_hours_for_day_from_api(date=date, city=city)

# будем отслеживать УВ-индекс, если он будет больше или равен 3 - будем выводить сообщение "Воспользуйтесь солнцезащитным кремом"

#-------------------------------------------------------------


#САМЫЙ ПОСЛЕДНИЙ ШАГ! ДЕКОРАТОР! запрос нужно сделать так, что он проходил несколько раз, поэтому надо завернуть в декоратор обработку ошибки, чтоб он щее раз пошел в апи, сначала через 5 секунд, потом через 30

def retry(func):
    def wrapper_retry(*args, **kwargs):
        retries = [5,30]
        for seconds in retries:
            try:
                return func(*args, ** kwargs)
            except RequestException:
                print(f"Failed to get data. Retrying in {seconds=}")
                time.sleep(seconds)
        return func(*args, ** kwargs)

    return wrapper_retry

#оборачиваем в ДЕКОРАТОР 
@retry 
def get_get_weather_by_hours_for_day_from_api(*, date: str, city: str) -> list[dict]:
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}/{date}?unitGroup=us&key={API_KEY}"
    respons = requests.get(url)
    weather_by_days = respons.json()["days"]  #достаем структуру по дням
    weather_by_hours = weather_by_days[0]["hours"]  #достаем структуру по часам

    return weather_by_hours

#пишем функцию, которая преегонит темп. по Фаренгейту в темп. по Цельсию 
def fahrenheit_to_celsius(*, fahrenheit_temperature: float) -> int:
    return round((fahrenheit_temperature - 32) * 5 / 9) #формула перевода температуры


# достаем опасные часы   
def get_dangerous_hours(*, weather_by_hour: list[dict]) -> list[dict]:
    dangerous_hours = []
    for weather in weather_by_hour:
        uvindex = weather["uvindex"]
        time = weather["datetime"]
        celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature=weather["temp"])
        if uvindex >= 3:
            dangerous_hours.append({"time": time, "uvindex": uvindex, "temperature": celsius_temperature})

    return dangerous_hours

date = "2023-08-04"
city = "London, UK"
weather_by_hour = get_get_weather_by_hours_for_day_from_api(date=date, city=city)
dangerous_hours = get_dangerous_hours(weather_by_hour=weather_by_hour) 
print(dangerous_hours)



