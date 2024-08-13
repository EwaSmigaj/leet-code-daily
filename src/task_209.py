from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rev(None, head)

    def rev(self, prev, head):
        if head is not None:
            tmp = head.next
            head.next = prev
            if tmp:
                tmp2 = tmp.next
                tmp.next = head
                return self.rev(tmp, tmp2)
        elif prev is not None:
            return prev
        return head
