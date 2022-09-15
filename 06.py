class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def palindrom_checker(str):
            return str == str[::-1]

        s_len = len(s)

        for check_num in range(s_len, 0, -1):
            for j in range(s_len-check_num+1):
                if palindrom_checker(s[j:j+check_num]):
                    return s[j:j+check_num]

'''
Runtime: 6427 ms, faster than 11.52% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.8 MB, less than 90.03% of Python3 online submissions for Longest Palindromic Substring.

이 경우는 투포인터로 푸는 것이 빠름
최초 등장이 필요한 2/3 길이 팰린드롬을 찾는 것이 관건
'''