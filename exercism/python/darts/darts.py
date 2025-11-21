def score(x, y):
    result = (x ** 2 + y **2) ** 0.5
    if result <= 1:
        return 10
    if result <= 5:
        return 5
    if result <= 10:
        return 1
    return 0

print(score(-9, 9)) #12 = 0 очков

print(score(-5, 0)) #5 =   5 очков

print(score(0, 0)) #0   = 10 очков

print(score(3.6, -3.6)) #5,091 = поэтому 1 очко
