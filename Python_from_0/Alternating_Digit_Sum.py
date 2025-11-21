
#2544. Alternating Digit Sum
def alternatingSum(nums: list[int]) -> int:
    # 1
    # result = 0
    # for char in nums:
    #     if char in nums[0: len(nums): 2]:  #[0],[2]
    #         result += char
    #     if char in nums[1: len(nums): 2]:  #[1],[3]
    #         result -= char
    # return result

    # 2
    # result = []
    # for char in nums:
    #     if char in nums[0: len(nums): 2]:  #[0],[2]
    #         result.append(char)
    #     if char in nums[1: len(nums): 2]:  #[1],[3]
    #         result.append(-char)
    # return sum(result)

    # 3
    # result_1 = []
    # result_1.append(nums[0: len(nums): 2])
    # # print(result_1)
    # result_2 = []
    # result_2.append(nums[1: len(nums): 2])
    # # print(result_2)
    # return sum(result_1[0]) - sum(result_2[0])
    
    #4
    return sum((nums[0: len(nums): 2])) - sum((nums[1: len(nums): 2]))

    

# O(n)(часть списка = срезы) + O(n)(суммы)  = O(n) - линейная 

print(alternatingSum(nums=[1,3,5,7])) 

print(alternatingSum(nums=[100]))

print(alternatingSum(nums=[1,1,1]))   #1

print(alternatingSum(nums=[1,1])) 


#ПЕРЕРЕШИВАТЬ В ОДИН ПРОХОД 



