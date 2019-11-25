# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node=ListNode(0)
        h=node
        c=0
        # ans=0
        while(l1 or l2):
            # ans=l1.val+l2.val
            val1=(l1.val if l1 else 0)
            val2=(l2.val if l2 else 0)
            digit=(val1+val2+c)%10
            c=(val1+val2+c)//10
            # digit=(val1+val2+c)%10
            h.next=ListNode(digit)
            h=h.next
            l1=(l1.next if l1 else None)
            l2=(l2.next if l2 else None)
        if(c):
            h.next=ListNode(c)
        return node.next
            
