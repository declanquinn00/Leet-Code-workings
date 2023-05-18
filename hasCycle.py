# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dictionary = {}
        while head is not None:
            if head not in dictionary:
                dictionary[head] = True
                head = head.next
            else:
                return True
        return False