# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        r={}
        c=0
        q=head
        while q:
            if q in r:
                return q
            r[q]=c
            c+=1
            q=q.next
        return None
        