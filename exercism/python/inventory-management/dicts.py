"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}                          #пустой словарь 

    for key in items:                       #перебираем с помощью цикла ключи в данных нам списке предметов 
        inventory.setdefault(key, 0)        #с помощью метода добавляем пару ключ и значение (0) в пустой словарь
        inventory[key] += 1                 #прибавляем +1 если повторяется
    return inventory
    
# print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for key in items:                     #перебираем с помощью цикла ключи в данных нам списке предметов 
        inventory.setdefault(key, 0)      #с помощью метода добавляем пару ключ и значение (0) в словарь
        inventory[key] += 1               #прибавляем +1 если повторяется
        # print(inventory)
    return inventory

# print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    # for key in items:
    #     # print(key)
    #     inventory.setdefault(key, 0)
    #     # print(inventory)
    #     if inventory[key] > 0:                 #ДОБАВЛЯЕМ УСЛОВИЕ О ТОМ, ЧТО ТОЛЬКО ЕСЛИ ЗНАЧЕНИНЕ СТРОГО > 0, ТО МОЖНО УМЕНЬШАТЬ - для того, чтобы не уйти в отрицательные числа 
    #         inventory[key] -= 1
    #     # if inventory[key] <= 0:
    #     #     inventory[key] = 0
    # return inventory

    for key in items:                                 #перебираем ключи, которые надо уменьшить в данном нам списке предметов 
        if key in inventory and inventory[key] > 0:   #проверяем наличие ключа и значение > 0
            inventory[key] -= 1                       #то уменьшаем значение на один
    return inventory                                  #Функция decrement_items должна изменять переданный ей словарь inventory напрямую, а не создавать новый. И, как мы уже знаем, она не должна добавлять в словарь элементы, которых раньше не было.

# print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"]))    

# print(decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"]))


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    # result = inventory.copy()        #Ваня, создала копию словаря, чтоб его изменить, т.к. сам словарь в цикле меня нельзя(?)
    
    # for key in inventory:            #перебираем с помощью цикла ключи в данных нам словарях
    #     if key in item:              #если ключ в предмете который дан
    #         result.pop(key)          #с помощью метода удаляем его
    # return result

    inventory.pop(item, None)          #
    return inventory

# print(remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))
# print(remove_item({"coal":2, "wood":1, "diamond":2}, "gold"))

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    # result = inventory.copy()                  #Ваня, создала копию словаря, чтоб его изменить, т.к. сам словарь в цикле меня нельзя(?)
    
    # for key, value in inventory.items():       #с помощью метода перебираем ключи и значения в ИНВЕНТАРЕ
    #     # print(key,value)
    #     if value <= 0:                         #если значение <=0 удалем его с помощью метода 
    #         result.pop(key)                    #удалем его с помощью метода 
    #     res = list(result.items())             #в новой переменной с помощью метода делаем пару кортеж (ключ,значение) и оборачиваем в список, ТАК ТРЕБУЕТ ЗАДАНИЕ
    # return res

    result = []                                  # добавляем в пустой список сразу нужные нам значения, ЭТОТ ПОДХОД ПРОЩЕ И БЫСТРЕЕ 

    for key, value in inventory.items():
        if value > 0:
            result.append((key, value))
    return result


# print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))
