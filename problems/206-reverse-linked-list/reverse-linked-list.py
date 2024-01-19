# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        p,q=head,None
        while p:
            temp=p.next
            p.next=q
            q=p
            p=temp
        return q
        