class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listnode_maker(input):
    if input == []:
        return None
    
    return ListNode(val=input.pop(0), next=listnode_maker(input))

list1 = listnode_maker([1, 2, 4])
list2 = listnode_maker([1, 3, 4])


def generate(list1, list2):
    val1 = list1.val
    val2 = list2.val

    if list1.val == None and list2.val == None:
        return None

    if val1<=val2:
        val1.next = generate(list1.next, list2)
        return val1
    else:
        val2.next = generate(list1, list2.next)
        return val2
    
result = generate(list1, list2)

list1 = [1,2,43,4]
