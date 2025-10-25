def equilateral(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0: #здесь OR потому что вернет нам ретерн, если хотя бы одно = 0
        return False 
    if a + b >= c and b + c >= a and a + c >= b:  #AND ПОТОМУ ЧТО НАДО ЧТОБ ВСЕ УСЛОВИЯ БЫЛИ TRUE,проверка , что треугольник существует
        return a == b == c     #все стороны равны
    return False
    
     

def isosceles(sides):
    a, b, c = sides
    if a + b >= c and b + c >= a and a + c >= b:   #проверка , что треугольник существует 
        return  a==b or a==c or b==c            #две стороны равны, #здесь OR потому что вернет нам ретерн, если хотя бы одно равно tRUE
    return False


def scalene(sides):
    a, b, c = sides
    if a + b >= c and b + c >= a and a + c >= b:
        return a != b and b != c and a != c #все стороны не равны, AND ПОТОМУ ЧТО НАДО ЧТОБ ВСЕ УСЛОВИЯ БЫЛИ TRUE
    return False 
