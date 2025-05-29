# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        temp = head
        temp2 = head
        length = 1
        while temp2.next:
            temp2 = temp2.next
            length += 1

        stop = length - n - 1
        if stop == -1:
            head = head.next
            temp = 0
        while temp and stop != 0:
            temp = temp.next
            stop -= 1

        if not temp:
            temp = None
        elif temp.next:
            temp3 = temp.next
            temp.next = temp.next.next
            temp3.next = None
        return head


