# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head: return head
        l=[head]
        temp=head
        while temp.next:
            l.append(temp.next)
            temp=temp.next
        new1=ListNode(l[0].val)
        curr=new1
        for i in range (2,len(l),2):
            curr.next=ListNode(l[i].val)
            curr=curr.next
        for i in range (1,len(l),2):    
            curr.next=ListNode(l[i].val)
            curr=curr.next
        return new1


        