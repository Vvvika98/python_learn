def is_isogram(string):
    string = string.replace("-", "").replace(" ", "").lower().strip() #проще сделать все операции над строкой сразу, чем в каждом случае заново
    return len(string) == len(set(string))





# print(is_isogram("six-year-old"))

# print(is_isogram("Emily Jung Schwartzkopf"))