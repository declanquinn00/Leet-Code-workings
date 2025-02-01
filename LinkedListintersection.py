class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA



    return a