# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        r1,r2=0,0
        p,q,r=l1,l2,l1
        while p:
            r1=r1*10+p.val
            p=p.next
        while q:
            r2=r2*10+q.val
            q=q.next
        r=[int(i) for i in str(r1+r2)]
        j=1
        ans=ListNode(r[0])
        temp=ans
        while j<len(r):
            n2=ListNode(r[j])
            temp.next=n2
            temp=n2
            j+=1
        temp.next=None
        return ans
        