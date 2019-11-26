# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA:
            return None
        if not headB:
            return None
        if headA==headB:
            return headA
        if not headA.next and not headB.next:
            return None
        currA=headA
        currB=headB
        while(currA.next):
            currA=currA.next
        endA=currA
        currA.next=headB
        slow=headA
        fast=headA
        while(fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                break
        if(slow!=fast):
          endA.next=None
          return None
        currA=headA
        while(currA!=fast):
            currA=currA.next
            fast=fast.next
        endA.next=None
        return currA
            
