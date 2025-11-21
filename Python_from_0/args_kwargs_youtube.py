#ARGS #KWARGS 
#--------------------------------------------------------------------------------

# *args 

def add_all(*args):   #class tuple ПОЗИЦИАННЫЕ АРГУМЕНТЫ 
    summary = 0
    for num in args:
        summary += num
    return summary


# print(add_all(1,2,3))

#если два списка необходимо слодитьиспользуя функцию выше 

values = [1,2,3,4,5]
other_values = [6,7,8,9,10]


print(add_all(*values, *other_values))

#--------------------------------------------------------------------------------

#когда необходимо передать именованные аргументы

def introduce(**kwargs): #class dictionary ИМЕНОВАННЫЕ (КЛЮЧЕВЫЕ АРГУМЕНТЫ)
    #в качестве аргументов можно передавать любое кол-во поименнованных аргументов 
    for key, value in kwargs.items():
        print(key)
        print(value)


#имеем словарь и нужно его запихнуть в функцию в качестве аргументов 

person = {
    "city" : "New York",
    "age" : 30,
    "name": "John"
}

#в функцию передаем словарь в качестве аргумента, добавив ** - распаковываем словарь

print(introduce(**person))

#--------------------------------------------------------------------------------

#сделаем функцию, объединив все возможные варианты аргументов 

def func_with_all_arguments(x: int, y: int, *args, value: int = 6, **kwargs):   #арги, кварги, дефолтное 
    print(x,y)
    print(args)
    print(value)
    print(kwargs)


#вызываем функцию

print(func_with_all_arguments(1,2, 3, 4, 5, **person))   #нельзя писать х=1, у=2 и дальше 3,4,5 либо args в переменную либо без именованных аргументов 

#--------------------------------------------------------------------------------

# напишем функцию, которая модифицирует словарь и первым аргументом возвращает модифицированный словарь, а вторым - был ли словарь модифицированный
def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modifide = False            #изначально форс т.к. ничего еще не изменилось 

    for key, value in kwargs.items():          #итерируемся по ключам и значениям "модификаций" 
        if old_dict.get(key) != value:            #нужно проверить есть ли значение с таким ключом в старом словаре
            old_dict[key] = value              #используя метод ГЕТ присваиваем новые значения в старый словарь
            is_modifide = True                 #И ТОГДА меняем переменную "модификация" на тру
    return old_dict, is_modifide               #возвращаем словарь и переменную модификация = да или нет


product = {"id" : 1, "name" : "Laptop", "price" : 999.99}    #старый словарь

# structure = modify_dict(old_dict=product, in_stock=True)     #переменная структура, в которой старый словарь и КВАРГС - модификация
structure = modify_dict(old_dict=product, name="Laptop")  
print(structure)
print(type(structure))   

#можно распаковать с разные переменные 
product, is_modifide = modify_dict(old_dict=product, name="Laptop") 
print(product)
print(is_modifide)


