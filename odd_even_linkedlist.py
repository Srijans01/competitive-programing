# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        odd=head
        even=head.next
        evenhead=even
        while(even and even.next and even.next.next):
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        if(even.next):
            odd.next=even.next
            odd=odd.next
            even.next=None
        odd.next=evenhead
        return head
