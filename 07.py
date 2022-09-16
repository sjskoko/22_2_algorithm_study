class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match_num_dict = {}

        for i, num in enumerate(nums):
            match_num = target - num
            match_num_dict[match_num] = i

        for i, num in enumerate(nums):
            try:
                j = match_num_dict[num]
                if i != j:
                    return [i, j]
            except:
                pass

'''
Runtime: 128 ms, faster than 45.65% of Python3 online submissions for Two Sum.
Memory Usage: 15.5 MB, less than 8.83% of Python3 online submissions for Two Sum.
'''