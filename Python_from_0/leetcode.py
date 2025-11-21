def shuffle(nums: list[int], n: int) -> list[int]:
    result = []
    for i in range(0,n):
        result.append(nums[i])
        result.append(nums[n+i])
    return result
        
print(shuffle([2,5,1,3,4,7], 3))        #[2,3,5,4,1,7]  