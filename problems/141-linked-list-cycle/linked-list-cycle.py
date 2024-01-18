# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        r=[]
        q=head
        while q not in r and q!=None:
            r.append(q)
            q=q.next
        return q!=None
        