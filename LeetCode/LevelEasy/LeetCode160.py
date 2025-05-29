# 160. Intersection of Two Linked List

class Solution:
    def getIntersectionNode(self, headA, headB):
        temp1  = headA
        temp2 = headB
        while temp1 != temp2:
            temp1 = headB if not temp1 else temp1.next
            temp2 = headA if not temp2 else temp2.next
        return temp1

