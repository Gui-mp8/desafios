from typing import Optional, ListNode

def hasCycle(head: Optional[ListNode]) -> bool:
    """
    Tortoise and Hare algorithm

    The idea is that we create two pointers, a slow one and a fast one.
    The slow pointer traverses the linked list 1 node at a time, while the fast pointer traverses the linked list 2 nodes at a time.
    If at some point the two pointers meet on the same node, then that means a cycle exists.

    """
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer is fast_pointer:
            return True
    return False
