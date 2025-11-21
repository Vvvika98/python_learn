
def f1(arr):
    l1 = sorted(arr)
    l2 = [i for i in l1 if i < 0.5]
    return [i * i for i in l2]

# O(n log n) (сортировка) + O(n) (фильтрация) + O(n) (возведение в квадрат)
# Поскольку O(n log n) растет быстрее, чем O(n), мы можем сказать, что доминирующая сложность – O(n log n).


def f2(arr):
    l1 = [i for i in arr if i < 0.5]
    l2 = sorted(l1)
    return [i * i for i in l2]

#O(n) (фильтрация) + O(n log n) (сортировка) + O(n) (возведение в квадрат)
# Поскольку O(n log n) растет быстрее, чем O(n), мы можем сказать, что доминирующая сложность – O(n log n).



def f3(arr):
    l1 = [i * i for i in arr]
    # l2 = sorted(l1)    #ОНО НЕ ИСПОЛЬЗУЕТСЯ )))
    return [i for i in l1 if i < (0.5 * 0.5)]

#O(n) (возведение в квадрат) + O(n) (фильтрация.
#Доминирующий член – O(n).



'''
Второе наибольшее число в списке
Напишите функцию, которая найдёт в списке число, которое являе
тся вторым наибольшим в этом списке.
'''
def find_second_maximum_num(arr: list[int]):
    if len(arr) == 0:  #O(1)
        return None
    arr2 = set(arr)     #O(n)
    if len(arr2) == 1:  #O(1)
        return None
    max_num1 = max(arr2)  #O(n)
    arr2.remove(max_num1) #O(1)
    max_num2 = max(arr2)  #O(n)
    return max_num2

#Доминирующий член – O(n)


print(find_second_maximum_num([3,7,9,11,3,5,1]))


def alternatingSum(nums: list[int]) -> int:
    return sum((nums[0: len(nums): 2])) - sum((nums[1: len(nums): 2]))

# O(n)(часть списка = срезы) + O(n)(суммы)  = O(n) - линейная 

print(alternatingSum(nums=[1,3,5,7]))

print(alternatingSum(nums=[100]))

print(alternatingSum(nums=[1,1,1]))   #1

print(alternatingSum(nums=[1,1])) 
