class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(self, head):
    cpy = head
    while cpy != None:
        while cpy.next and cpy.val == cpy.next.val:
            cpy.next = cpy.next.next
        cpy = cpy.next
    return head
