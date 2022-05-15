class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(list1, list2):
    outputList = ListNode(None, None)
    tmpNode = outputList
    while list1 != None and list2 != None:
        if (list1.val <= list2.val):
            tmpNode.next = list1
            list1 = list1.next

        elif (list1.val > list2.val):
            tmpNode.next = list2
            list2 = list2.next
        tmpNode = tmpNode.next

    if (list1 == None):
        while list2 != None:
            tmpNode.next = list2
            list2 = list2.next
            tmpNode = tmpNode.next
    elif (list2 == None):
        while list1 != None:
            tmpNode.next = list1
            list1 = list1.next
            tmpNode = tmpNode.next
    return outputList.next
