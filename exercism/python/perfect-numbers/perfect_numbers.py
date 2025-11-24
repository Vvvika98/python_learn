def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    aliquot_sum = sum([num for num in range(1, number) if number % num == 0])
    
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    # print(aliquot)
    if number == aliquot_sum:
        return "perfect"
    if number < aliquot_sum:
        return "abundant"
    return "deficient"




# print(classify(6))  #"perfect"

# print(classify(12)) #"abundant"

# print(classify(8))  #"deficient"

# print(classify(0))  #valueError





