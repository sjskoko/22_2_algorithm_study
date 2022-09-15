import re
from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_list = re.findall('[\w\d]+', paragraph.lower())
        word_dict = defaultdict(int)

        for word in word_list:
            word_dict[word] += 1

        for ban_word in banned:
            try:
                del word_dict[ban_word]
            except:
                pass

        return max(word_dict, key=word_dict.get)

'''
Runtime: 66 ms, faster than 35.21% of Python3 online submissions for Most Common Word.
Memory Usage: 13.8 MB, less than 82.54% of Python3 online submissions for Most Common Word.

defaultdictionary 및 max() 사용

Collection의 Counter 사용해도 좋음
'''