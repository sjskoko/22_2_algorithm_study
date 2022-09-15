from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strs_dict = defaultdict(list)

        for str in strs:
            sstr = sorted(str)
            strs_dict[''.join(sstr)].append(str)

        result = []
        for i in strs_dict:
            result.append(strs_dict[i])
            
        return result

'''
dictionary.value() 를 사용 안함
return에서 strs_dict.value()를 사용하는 것이 효과적
'''