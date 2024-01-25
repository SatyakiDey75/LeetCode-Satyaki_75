# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None
        p=head
        # l=[]
        # while p:
        #     l.append(p.val)
        #     p=p.next
        # l1=sorted(list(set(l)))
        # h1=ListNode(l1[0])
        # t=h1
        # for i in range (1,len(l1)):
        #     h2=ListNode(l1[i])
        #     t.next=h2
        #     t=h2
        # t.next=None
        # return h1
        while p:
            if p.next and p.val==p.next.val:
                p.next=p.next.next
            else:
                p=p.next
        return head