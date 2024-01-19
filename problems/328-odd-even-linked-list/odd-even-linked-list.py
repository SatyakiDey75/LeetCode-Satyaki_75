# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        r,q,p,i=[],head,head,0
        while p:
            r.append(p.val)
            p=p.next
        r=r[::2]+r[1::2]
        while i<len(r):
            q.val=r[i]
            q=q.next
            i+=1
        return head
