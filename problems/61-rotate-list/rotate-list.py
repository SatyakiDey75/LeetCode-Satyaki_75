# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        l=[head]
        temp=head
        i=0
        if k==0 or not temp: return head
        while temp.next:
            l.append(temp.next)
            i+=1
            temp=temp.next
        k=k%(i+1)
        head1=None
        i=len(l)-1
        for j in range (k):
            head1=ListNode(l[i].val)
            l[i-1].next=None
            head1.next=head
            head=head1
            i-=1
            if i<0:
                i=len(l)-1
        return head