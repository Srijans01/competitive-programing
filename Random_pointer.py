"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        curr=head
        while(curr):
            n1=Node(curr.val,None,None)
            tmp=curr.next
            n1.next=tmp
            curr.next=n1
            curr=tmp
        prev=head
        while(prev):
            curr=prev.next
            if(prev.random):
                curr.random=prev.random.next
            prev=curr.next
        o_head=head
        new_head=head.next
        f_head=new_head
        
        while(o_head and o_head.next and new_head and new_head.next):
            o_head.next=o_head.next.next
            new_head.next=new_head.next.next
            o_head=o_head.next
            new_head=new_head.next
        o_head.next=None
        new_head.next=None
        
        return(f_head)
