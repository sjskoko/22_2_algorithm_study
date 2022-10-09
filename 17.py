class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listnode_maker(input):
    if input == []:
        return None
    
    return ListNode(val=input.pop(0), next=listnode_maker(input))

head = listnode_maker([1, 2, 3, 4])

result = head

while result and result.next:

    result.val, result.next.val = result.next.val, result.val
    result = result.next.next

print(head.val)
print(head.next.val)
print(head.next.next.val)


####################  

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head

        while result and result.next:

            result.val, result.next.val = result.next.val, result.val
            result = result.next.next
            
        return head

'''
Runtime: 64 ms, faster than 23.42% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 14 MB, less than 19.73% of Python3 online submissions for Swap Nodes in Pairs.
재귀 구조 다시 공부
'''