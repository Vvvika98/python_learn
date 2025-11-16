def leap_year(year):
    # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #     return True
    # return False 

    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


print(leap_year(2000))  #(T F) T = T

print(leap_year(1900))  #(T F) F = F 

print(leap_year(2025))  #(F T) F = F