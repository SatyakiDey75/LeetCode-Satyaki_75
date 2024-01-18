# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def rotate(l,d):
    l1=[]
    for i in range (len(l)-d,len(l)):
        l1.append(l[i])
    for i in range (0,len(l)-d):
        l1.append(l[i])
    return l1

class Solution(object):
    def rotateRight(self, head, k):
        if head==None:
            return None
        r=[]
        p,q=head,head
        while p!=None:
            r.append(p.val)
            p=p.next
        r1=rotate(r,k%len(r))
        i=0
        while q!=None and i<len(r1):
           q.val=r1[i]
           i+=1
           q=q.next
        return head
        