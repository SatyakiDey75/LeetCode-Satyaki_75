# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if head==None:
            return None
        r=[]
        p,q=head,head
        while p!=None:
            r.append(p.val)
            p=p.next
        while val in r:
            r.remove(val)
        if r==[]:
            return None
        i=0
        while i<len(r)-1:
            q.val=r[i]
            q=q.next
            i+=1
        q.val=r[-1]
        q.next=None
        return head
        