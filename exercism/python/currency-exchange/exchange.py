"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate

print(exchange_money(127.5, 1.2))


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value

print(get_change(127.5, 120))


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    return denomination * number_of_bills 


print(get_value_of_bills(5, 128))


def get_number_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return amount // denomination


print(int(get_number_of_bills(127.5, 5)))


def get_leftover_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    return amount % denomination


print(get_leftover_of_bills(127.5, 20)) #не сразу поняла почему результат 7.5


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    new_exchange_rate = exchange_rate * (1 + spread / 100)   #рассчитываем новый курс с учетом спреда 
    after_exchange = exchange_money(budget, new_exchange_rate)  #сумма после обмена 
    bills = get_number_of_bills(after_exchange, denomination) #используя предыдущую функцию деньги после отбмена / на номинал купюры 
    return get_value_of_bills(denomination, bills) #высчитали сколько денег (сумма) получится в заданном номинале 
    

print(exchangeable_value(127.25, 1.20, 10, 20))

print(exchangeable_value(127.25, 1.20, 10, 5))
