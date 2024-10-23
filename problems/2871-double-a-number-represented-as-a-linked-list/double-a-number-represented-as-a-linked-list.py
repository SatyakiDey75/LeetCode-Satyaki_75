# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s=0
        orgHead=head
        while head:
            s=s*10+head.val
            head=head.next
        head2=orgHead
        i=0
        l=list(str(s*2))
        while head2.next:
            head2.val=int(l[i])
            print("Bye",l[i])
            i+=1
            head2=head2.next
        head2.val=int(l[i])
        i+=1
        while i<len(l):
            print("Hello",l[i])
            head2.next=ListNode(int(l[i]))
            head2=head2.next
            i+=1
        return orgHead