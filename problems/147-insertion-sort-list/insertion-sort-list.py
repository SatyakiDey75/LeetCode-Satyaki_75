# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        r=[]
        h1=head
        h2=head
        while (h1!=None):
            r.append(h1.val)
            h1=h1.next
        r.sort()
        i=0
        while (h2!=None):
            h2.val=r[i]
            h2=h2.next
            i+=1
        return head
        