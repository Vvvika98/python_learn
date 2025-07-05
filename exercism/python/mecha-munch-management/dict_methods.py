"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for key in items_to_add:
        # print(key)
        if key in items_to_add:
            current_cart.setdefault(key, 0)
            current_cart[key] += 1
    return current_cart

# print(add_item({'Banana': 3, 'Apple': 2, 'Orange': 1}, ('Apple', 'Apple', 'Orange', 'Apple', 'Banana')))
# print(add_item({'Banana': 3, 'Apple': 2, 'Orange': 1}, ['Banana', 'Orange', 'Blueberries', 'Banana']))

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    return dict.fromkeys(notes, 1)
    
# print(read_notes(('Banana','Apple', 'Orange')))
# print(read_notes(['Blueberries', 'Pear', 'Orange', 'Banana', 'Apple']))

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    
    ideas |= recipe_updates
    return ideas

    # ideas.update(recipe_updates)
    # return ideas

# print(update_recipes(
#     {'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
#      'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
#     (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),)
#     ))

# print(update_recipes(
#     {'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
#     'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1},
#     'Pasta Primavera': {'Eggs': 1, 'Carrots': 1, 'Spinach': 2, 'Tomatoes': 3, 'Parmesan': 2, 'Milk': 1, 'Onion': 1}},
#     [('Raspberry Pie', {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2}),
#     ('Pasta Primavera', {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1}),
#     ('Blueberry Crumble', {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3})]
#     ))

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    result = dict(sorted(cart.items()))
    return result

# print(sort_entries({'Banana': 3, 'Apple': 2, 'Orange': 1}))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    result = {}                                       #создаем пустой словарь
    

    for keys, value in cart.items():                  #перебираем ключи и значения в словаре
        aisle_refrigerator = aisle_mapping[keys]      #получаем значения из второго словаря в переменную #Я НЕ ЗНАЛА ЧТО ПЕРЕБИРАЯ ОДИН СЛОВАРЬ МОЖНО ССЫАТЬ ТАКЖЕ НА ДРУГОЙ Если ключи такие же?
        # print(aisle_refrigerator)
        result[keys] = [value, *aisle_refrigerator]   #добавляем через присвоение ключ и объединенные значения с распаковкой
    
    """
     Элементы списка aisle_refrigerator, распакованные с помощью оператора *.  
     Это означает, что если aisle_refrigerator равен ['Aisle 5', False], то это эквивалентно написанию [value, 'Aisle 5', False].
     """

    return dict(sorted(result.items(), reverse=True))


# print(send_to_store({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},{'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    # result = {}

    # dict_1 = dict(sorted(fulfillment_cart.items()))      #отсортировала первый словарь
    # # print(dict_1)
    # dict_2 = dict(sorted(store_inventory.items()))       #отсортировлаа второй словарь 
    # # print(dict_2)

    # for key, value in dict_2.items():            #перебрали ключи и значения в инвентаре магазина
    #     # print(key,*value)
    #     if value[0] > 0:
    #         value_list_2 = dict_2[key]
    #         # print(*value_list_2)
    #         first_element_2 = value_list_2[0]
    #         # print(first_element_2)
    #         value_list_1 = dict_1[key]
    #         # print(*value_list_1)
    #         first_element_1 = value_list_1[0]
    #         res = first_element_2 - first_element_1
    #         # print(res)
    #         if res == 0:
    #             res = 'Out of Stock'
    #         # print(res)
    #         d_element = value_list_2[1:2]
    #     result[key] = [res, *d_element]
    # return result


    for key, value in fulfillment_cart.items():
        first_element_2 = store_inventory[key][0]
        # print(first_element_2)
        first_element_1 = fulfillment_cart[key][0]
        # print(first_element_1)
        element = first_element_2 - first_element_1
        print(element)
        if element == 0:
            element = 'Out of Stock'
        store_inventory[key][0] = element
        # result[key] = [element, *store_inventory[key][1:]]             #новый словарь не нужен 
    return store_inventory

print(update_store_inventory({'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},
{'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]}))

# {'Banana': [12, 'Aisle 5', False], 
# 'Apple': [10, 'Aisle 4', False], 
# 'Orange': ['Out of Stock', 'Aisle 4', False], 
# 'Milk': [2, 'Aisle 2', True]}
