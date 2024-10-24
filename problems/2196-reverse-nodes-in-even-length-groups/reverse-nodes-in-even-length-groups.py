# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head
        l, grp = [], 1
        while temp:
            sub = []
            for i in range (grp):
                if temp:
                    sub.append(temp.val)
                    temp=temp.next
                else: break
            grp+=1
            l.append(sub)
        for i in range (len(l)):
            if len(l[i]) % 2 == 0:
                l[i]= l[i][::-1]
        new_l = [j for i in l for j in i]
        head1 = ListNode(new_l[0])
        temp1 = head1
        for i in range (1, len(new_l)):
            temp1.next = ListNode(new_l[i])
            temp1 = temp1.next
        return head1