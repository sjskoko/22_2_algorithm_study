class Solution:
    def trap(self, height: List[int]) -> int:

        land_len = len(height)
        water = 0
        point_hight_info = {}

        max_height = max(height)
        max_idx = []

        now_max = 0
        for idx, h in enumerate(height):
            if h == max_height:
                max_idx.append(idx)
            if h > now_max:
                point_hight_info[idx] = h
                now_max = h


        max_height_num = len(max_idx)

        first_max_idx = max_idx[0]
        last_max_idx = max_idx[-1]
        now_max = 0

        # 일렬 진행 max - h 계산, last_max_idx 까지
        for idx, h in enumerate(height[:last_max_idx+1]):
            if h > now_max:
                now_max = h
            water += now_max - h

        now_max = 0
        for fidx, h in enumerate(reversed(height[last_max_idx+1:])):
            idx = land_len - fidx -1
            if h > now_max:
                now_max = h
            water += now_max-h

        return water


'''
Runtime: 237 ms, faster than 38.23% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 16.6 MB, less than 7.16% of Python3 online submissions for Trapping Rain Water.
'''
# Another answer
class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max),\
                                    max(height[right], right_max)
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

'''
이 방법이 메모리는 더 효율적
시간 역시 빠르게 계산 가능
투포인터에 익숙해지자
'''