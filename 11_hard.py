import enum
from string import punctuation


nums = [-1,1,0,-3,3]
result = [1 for _ in nums]
for i, num in enumerate(nums):
    for j, p_num in enumerate(result):
        if j == i:
            result[j] = p_num
        else:
            result[j] *= num

print(result)

########################
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in nums]
        for i, num in enumerate(nums):
            for j, p_num in enumerate(result):
                if j == i:
                    result[j] = p_num
                else:
                    result[j] *= num
                    
        return result

'''
Time Limit Exceeded

O(n) 이내에 풀이 실패 
'''

###########################

nums = [-1,1,0,-3,3]
result = []
left_mul = 1
for i in range(len(nums)):
    result.append(left_mul)
    left_mul *= nums[i]

right_mul = 1
for i in range(len(nums)-1, -1, -1):
    result[i] *= right_mul
    right_mul *= nums[i]

print(result)

'''
Runtime: 488 ms, faster than 35.56% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21.1 MB, less than 95.54% of Python3 online submissions for Product of Array Except Self.
'''