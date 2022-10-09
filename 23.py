import collections


class MyStack:

    def __init__(self):
        self.item = collections.deque()
        

    def push(self, x: int) -> None:
        self.item.appendleft(x)
        

    def pop(self) -> int:
        return self.item.popleft()

    def top(self) -> int:
        return self.item[0]
        

    def empty(self) -> bool:
        return len(self.item) == 0
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

'''
Runtime: 71 ms, faster than 5.49% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 14 MB, less than 75.21% of Python3 online submissions for Implement Stack using Queues.

deque 알아두기, 시간 복잡도 개선 필요
'''