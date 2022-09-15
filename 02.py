class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s[::-1]
        return s


'''
문제에서 공간복잡도가 O(1)로 제한되어있어,
s = s:[::-1]이 동작하지 않음
s[::] = s[::-1]과 같이 할 수 있지만, 내장 함수를 사용하는 것이 good'''