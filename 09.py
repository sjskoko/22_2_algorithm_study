class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        len_nums = len(nums)
        def sum_3num(space, target):
            nums_map = {}
            result = []
            for i, num in enumerate(space):
                if target - num in nums_map:
                    result.append([-target, target - num, num])
                nums_map[num] = i

            return result

        result = []
        for i, num in enumerate(nums[:-2]):

            sub_result = sum_3num(nums[i+1:], -num)
            for j in sub_result:
                if j not in result:
                    result.append(j)

        return result

'''
Runtime: 6340 ms, faster than 10.69% of Python3 online submissions for 3Sum.
Memory Usage: 19.1 MB, less than 8.48% of Python3 online submissions for 3Sum.

한번 Time Limit Exceeded 됨
메모리 용량은 크게 줄인 듯(교재 예제 248.2 MB)
'''
