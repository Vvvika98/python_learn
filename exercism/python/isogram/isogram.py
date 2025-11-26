def is_isogram(string):
    string = string.replace("-", "").replace(" ", "")
    return len(string.lower().strip()) == len(set(string.lower()))





# print(is_isogram("six-year-old"))

# print(is_isogram("Emily Jung Schwartzkopf"))