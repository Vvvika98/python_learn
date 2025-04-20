#функция с использованием цикла фор 
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
    
    prefixes = vocab_words[0] #вычисляем префикс 
    zero_list = [prefixes] #создаем "пустой" список и вначале добавляем префикс
    for index in range(1, len(vocab_words)): #запускаем цикл for, в котором берем слова в интревале 1-4 по len? range дает 1-3
        result = prefixes + vocab_words[index] #добавляем в каждому слову по индексу из цикла префикс и присваиваем это в переменную 
        zero_list.append(result) #используя метод добавляются полученные слова из цикла (по одному за каждый цикл)

    return ' :: '.join(zero_list) #используя метод добавляем разделитель в список, преобразуя его в строку с разделителем 

print(make_word_groups(['en', 'close', 'joy', 'lighten']))