# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        p,a,b=head,None,None
        while p!=None:
            b=p.next
            p.next=a
            a=p
            p=b
        return a
        