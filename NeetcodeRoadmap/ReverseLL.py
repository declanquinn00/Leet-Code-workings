# assume LL
def reverseList(head):
    # this step breaks the recursion
    if not head:
        return None

    # EDGE CASE this is the case if the list is a single node long
    newHead = head
    # recursive case
    if head.next:
        # newHead will be the last in the LL
        # I think this just returns the last head through the recursion
        newHead = reverseList(head.next)
        # this states the next nodes next value will be this one
        head.next.next = head
    # this destroyes the next link
    head.next = None

    return newHead