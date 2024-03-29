# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        # r=[]
        # q=head
        # while q not in r and q!=None:
        #     r.append(q)
        #     q=q.next
        # return q!=None

        # 100% beats:
        i,j=head,head
        while j and j.next:
            i=i.next
            j=j.next.next
            if i==j:
                return True
        return False
        