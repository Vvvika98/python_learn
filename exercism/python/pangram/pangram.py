def is_pangram(sentence):
    # count = 0
    alphabet = "abcdefghigklmnopqrstuvwxyz"
    # for char in sentence.lower():                #разобьем предложение на символы
    #     if char in alphabet:
    #         count += 1
    return set(alphabet).issubset(set(sentence.lower()))






print(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"))  #T

print(is_pangram(""))                                                                      #F

print(is_pangram("bcdefghijklmnopqrstuvwxyz"))                                             #F

print(is_pangram("abcdefghijklm ABCDEFGHIJKLM"))                                           #F

print(is_pangram("a quick movement of the enemy will jeopardize five gunboats"))           #F
 
print(is_pangram("five boxing wizards jump quickly at it"))                                #F

print(is_pangram("abcdefghijklmnopqrstuvwxyz"))  #T
 
print(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"))                           #F

print(is_pangram('"Five quacking Zephyrs jolt my wax bed."'))

