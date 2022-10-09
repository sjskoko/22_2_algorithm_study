nums = [6,2,6,5,1,2]

nums.sort()

result = 0
count = 0
for i in nums:
    if count % 2 == 0:
        result += i
    count += 1

print(result) # 9

####################

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        result = 0
        count = 0
        for i in nums:
            if count % 2 == 0:
                result += i
            count += 1
        
        return result

'''
Runtime: 790 ms, faster than 5.01% of Python3 online submissions for Array Partition.
Memory Usage: 16.8 MB, less than 21.53% of Python3 online submissions for Array Partition.
'''
    
#####################

nums = [6,2,6,5,1,2]

sum(sorted(nums)[::2])

# nums[::2] -> 2개씩 건너뛰면서 반환


