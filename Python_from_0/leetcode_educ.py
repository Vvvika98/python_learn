#Эффективное построение строк
# arr is a list of characters
def fn(arr):
    result = []
    for char in arr:
        # print(char)
        result.append(char)
    
    return "".join(result)



print(fn(['a', 'n', 'g', 'e', 'l']))  #"angel


#Префиксные суммы

''' — это последовательные накопленные суммы элементов массива, где каждый элемент показывает сумму всех элементов слева до него включительно.

- Наглядная аналогия: представь, что складываешь числа в корзину слева направо и после каждого добавления записываешь текущую общую сумму.

- Формула: prefix[i] = arr[0] + arr[1] + ... + arr[i]

Пример пошагово (очень просто):
- arr = [1, 2, 3, 4]
- prefix:
  - prefix[0] = 1
  - prefix[1] = 1 + 2 = 3
  - prefix[2] = 3 + 3 = 6
  - prefix[3] = 6 + 4 = 10
- Итого prefix = [1, 3, 6, 10] 
'''
def fn(arr):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])
    
    return prefix

