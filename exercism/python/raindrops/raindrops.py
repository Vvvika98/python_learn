def convert(number):
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    return result or str(number) #т.к. result = False (пусатя), вернется str(number)



    # if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
    #     return "PlingPlangPlong"
    # elif number % 5 == 0 and number % 7 == 0:
    #     return "PlangPlong"
    # elif number % 3 == 0 and number % 5 == 0:
    #     return "PlingPlang"
    # elif number % 3 == 0 and number % 7 == 0:
    #     return "PlingPlong"
    # elif number % 3 == 0:
    #     return "Pling"
    # elif number % 5 == 0:
    #     return "Plang"
    # elif number % 7 == 0:
    #     return "Plong"
    # return str(number)



print(convert(1)) #1

print(convert(3)) #"Pling"

# print(convert(5)) #"Plang"

# print(convert(7)) #"Plong"


print(convert(105))

print(convert(21)) #"PlingPlong"