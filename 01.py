import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        eng_int_com = re.compile(r'[^a-z^A-Z^0-9]*')
        m = eng_int_com.sub('',s)
        m_l = m.lower()
        return m_l == m_l[::-1]

'''
정규식 적용에 다소 시간 소요됨 -> .lower() method를 먼저 사용했다면 풀이 시간을 더 줄일 수 있음
컴파일이 불필요한 경우에는 만들지 말 것(자주 사용해야 하는 경우에는 만들 것)'''
