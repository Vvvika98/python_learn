"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
    






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





def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """ Calculate total elapsed cooking time (prep + bake)
    :param - number of layers, elapsed bake time: int 
    :return: int - total elapsed time (in minutes) 

    A function that takes the actual number of layers 
    and the baking time as arguments and returns how many minutes it took.

    """
    
    return number_of_layers * PREPARATION_TIME + elapsed_bake_time


    
