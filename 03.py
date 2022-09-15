import re

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        
        str_logs = []
        num_logs = []

        log_object = re.compile(r"(?P<id>\w*\d*)\s(?P<logs>[\w\d\s]*)")

        for log in logs:
            log_cut = log_object.sub('\g<logs>', log)
            id_cut = log_object.sub('\g<id>', log)
            print(log_cut)

            try:
                int(log_cut[0])
                num_logs.append(log)
            except:
                str_logs.append([id_cut, log_cut])

        str_logs.sort(key=lambda x: (x[1], x[0]))

        str_logs = [' '.join(i) for i in str_logs]


        return str_logs + num_logs


'''
sub 메서드를 사용할 때 참조 구문을 사용할 수 있다. 다음 예를 보자.

>>> p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
>>> print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
010-1234-1234 park


'''
###