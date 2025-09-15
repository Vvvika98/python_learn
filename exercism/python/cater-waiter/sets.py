"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)
from sets_categories_data import example_dishes, EXAMPLE_INTERSECTION

def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    return dish_name, set(dish_ingredients)
    
# print(clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro']))

def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """
   
    if set(drink_ingredients).isdisjoint(ALCOHOLS):           #использую метод отсутстивя общих элементов (можно были и наоборот ч/з .intersection() - нахождение общих элементовЫ)
        return f'{drink_name} Mocktail'
    return f'{drink_name} Cocktail'

# print(check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber']))
# print(check_drinks('Shirley Tonic', ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 'sugar', 'club soda']))



def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: set - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """

   

    # if dish_ingredients.issubset(VEGAN):
    #     return f'{dish_name}: VEGAN'
    # if dish_ingredients.issubset(VEGETARIAN):
    #     return f'{dish_name}: VEGETARIAN'
    # if dish_ingredients.issubset(KETO):
    #     return f'{dish_name}: KETO'
    # if dish_ingredients.issubset(PALEO):
    #     return f'{dish_name}: PALEO'
    # if dish_ingredients.issubset(OMNIVORE):
    #     return f'{dish_name}: OMNIVORE'
    
    category_map = {'VEGAN': VEGAN, 'VEGETARIAN': VEGETARIAN, 'KETO': KETO, 'PALEO': PALEO, 'OMNIVORE': OMNIVORE}
    for category, ingredients in category_map.items():
        # print(category, ingredients)
        if dish_ingredients.issubset(ingredients):
            return f'{dish_name}: {category}'

    

# print(categorize_dish('Sticky Lemon Tofu', {'tofu', 'soy sauce', 'salt', 'black pepper', 'cornstarch', 'vegetable oil', 'garlic', 'ginger', 'water', 'vegetable stock', 'lemon juice', 'lemon zest', 'sugar'}))
##'Sticky Lemon Tofu: VEGAN'

# print(categorize_dish('Shrimp Bacon and Crispy Chickpea Tacos with Salsa de Guacamoef categorize_dishle', {'shrimp', 'bacon', 'avocado', 'chickpeas', 'fresh tortillas', 'sea salt', 'guajillo chile', 'slivered almonds', 'olive oil', 'butter', 'black pepper', 'garlic', 'onion'}))
##'Shrimp Bacon and Crispy Chickpea Tacos with Salsa de Guacamole: OMNIVORE'


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    # return dish[0], set(dish[1]).intersection(SPECIAL_INGREDIENTS)
    
    name, ingredients = dish
    return name, set(ingredients).intersection(SPECIAL_INGREDIENTS)
    
# print(tag_special_ingredients(('Ginger Glazed Tofu Cutlets', ['tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'])))

# #('Ginger Glazed Tofu Cutlets', {'garlic','soy sauce','tofu'})

# print(tag_special_ingredients(('Arugula and Roasted Pork Salad', ['pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts', 'balsamic vinegar', 'onions', 'black pepper'])))

#('Arugula and Roasted Pork Salad', {'pork tenderloin', 'blue cheese', 'pine nuts', 'onions'}))

def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """
    # res = set()
    # for i in dishes:
    #     # print(i)
    #     res.update(i)
    # return res

    return set.union(*dishes)
    
    
print(compile_ingredients([{'tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'},{'pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts','balsamic vinegar', 'onions', 'black pepper'},{'honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'}]))


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    # dishes = set(dishes)
    # appetizers = set(appetizers)

    # result = dishes.difference(appetizers)
    # return result

    return list(set(dishes) - set(appetizers))

# dishes =    ['Avocado Deviled Eggs','Flank Steak with Chimichurri and Asparagus', 'Kingfish Lettuce Cups',
#              'Grilled Flank Steak with Caesar Salad','Vegetarian Khoresh Bademjan','Avocado Deviled Eggs',
#              'Barley Risotto','Kingfish Lettuce Cups']
          
# appetizers = ['Kingfish Lettuce Cups','Avocado Deviled Eggs','Satay Steak Skewers',
#               'Dahi Puri with Black Chickpeas','Avocado Deviled Eggs','Asparagus Puffs',
#               'Asparagus Puffs']    
# print(separate_appetizers(dishes, appetizers))



def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """



    # all_ingredients = set()              #пустое множество 
    # for dish in dishes:                  #перебираем блюдо из всех блюд
    #     all_ingredients.update(dish)     #добавляем в общий список ингридентов
    # singl_ingredients = all_ingredients - intersection  #из всех ингридиентов удаляем все из КОНСТАНТЫ
    # return singl_ingredients                 

    return compile_ingredients(dishes) - intersection       


# print(singleton_ingredients(example_dishes, EXAMPLE_INTERSECTION)) 