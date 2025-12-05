def reverseList(head):
    curr_h = head
    while curr_h.next:
        next_h = curr_h.next
        curr_h.next = None
        curr_h.next.next = curr_h
        curr_h = next_h

    return curr_h
