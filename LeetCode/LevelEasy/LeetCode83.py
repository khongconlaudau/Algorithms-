# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next   # skip the duplicate
            else:
                temp = temp.next    # if no duplicate, moves one step forward
        return head


