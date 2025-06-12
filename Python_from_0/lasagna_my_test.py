"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    # bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time - вообще так делать не надо 
    # return bake_time_remaining - достаточно передать в ретерн ПОСЛЕ РЕТЕРН МОНО ПИСАТЬ ЧТО УГОДНО 

    return EXPECTED_BAKE_TIME - elapsed_bake_time


    
    
print(bake_time_remaining(elapsed_bake_time=30))





#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.

def preparation_time_in_minutes(number_of_layers: int):
    """ Calculate preparation time in minutes.

    :param number_of_layers: int - number of layers of lassagna 
    :return: int - preparation time (in minutes) 
    
    A function that takes the actual number of layers as an argument
    and returns how many minutes it took.
    
    Let's assume each layer takes 2 minutes to cook. 
    You might also consider defining a 'PREPARATION_TIME' constant.

    """
    
    return number_of_layers * PREPARATION_TIME

print(preparation_time_in_minutes(number_of_layers=2)) #наименование аргумента можно и не писать! но пока так проще к восприятию 


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """ Calculate total elapsed cooking time (prep + bake)
    :param - number of layers, elapsed bake time: int 
    :return: int - total elapsed time (in minutes) 

    A function that takes the actual number of layers 
    and the baking time as arguments and returns how many minutes it took.

    """
    
    return number_of_layers * PREPARATION_TIME + elapsed_bake_time 

print(elapsed_time_in_minutes(number_of_layers=3, elapsed_bake_time=20))
    


# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)

