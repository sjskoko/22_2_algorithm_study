class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listnode_maker(input):
    if input == []:
        return None
    
    return ListNode(val=input.pop(0), next=listnode_maker(input))

head = listnode_maker([1,2,2,1,2])

rev = None
slow = fast = head

while fast and fast.next:
    fast = fast.next.next
    rev, rev.next, slow = slow, rev, slow.next
if fast:
    slow = slow.next

while rev and rev.val == slow.val:
    slow, rev = slow.next, rev.next

print(not rev)