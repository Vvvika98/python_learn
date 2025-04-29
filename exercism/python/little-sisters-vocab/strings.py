"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return f"un{word}"

# print(add_prefix_un("happy"))
# print(add_prefix_un("manageable"))


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    
    # prefixes = vocab_words[0] #вычисляем префикс 
    # zero_list = [prefixes] #создаем "пустой" список и вначале добавляем префикс
    # for index in range(1, len(vocab_words)): #запускаем цикл for, в котором берем слова в интревале 1-4 по len? range дает 1-3
    #     result = prefixes + vocab_words[index] #добавляем в каждому слову по индексу из цикла префикс и присваиваем это в переменную 
    #     zero_list.append(result) #используя метод добавляются полученные слова из цикла (по одному за каждый цикл)

    # return ' :: '.join(zero_list) #используя метод добавляем разделитель в список, преобразуя его в строку с разделителем 

    prefix = vocab_words[0] #вычисляем префикс 
    result = [prefix] #пустой список для результата
    for word in vocab_words[1:]:
        result.append(f"{prefix}{word}")
    return ' :: '.join(result)


print(make_word_groups(['en', 'close', 'joy', 'lighten']))
print(make_word_groups(['pre', 'serve', 'dispose', 'position']))
print(make_word_groups(['auto', 'didactic', 'graph', 'mate']))
print(make_word_groups(['inter', 'twine', 'connected', 'dependent']))


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    word = word[:-4] #обрезали слово без суффикса 
    if word[-1] == "i": #выбрали с помощью индекса последнюю букву обрезанного слова 
        return word[:-1] + "y" #т.к. полуоткрытый интервал последнее значение среза не входит и к слову добавляем букву 
    else:
        return word
    print(word)

    
    word = word[:-4]
    if word.endswith("i"): #новый метод 
        return word[:-1] + "y"
    return word
    print(word)

# print(remove_suffix_ness("heaviness"))


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    
    return sentence.strip(".").split()[index] + "en" #можно применять несколько методов одновременно 
    
    
print(adjective_to_verb('I need to make that bright.', -1))  

print(adjective_to_verb('It got dark as the sun set.', 2))  
