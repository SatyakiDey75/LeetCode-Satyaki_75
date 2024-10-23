# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """
        temp=head
        len_lnkd=0
        arr=[]
        while temp:
            len_lnkd+=1
            temp=temp.next
        n=len_lnkd // k
        r=len_lnkd % k
        arr=[None]*k
        curr=head
        for i in range (k):
            arr[i]=curr
            size=n+(1 if i<r else 0)
            for i in range (size-1):
                curr=curr.next
            if curr:
                temp=curr.next
                curr.next=None
                curr=temp
        return arr

        # for i in range (k):
        #     if temp:
        #         head1=ListNode(temp.val)
        #         temp1=head1
        #         temp=temp.next
        #         for j in range (n-1):
        #             temp1.next=ListNode(temp.val) 
        #             temp1=temp1.next
        #             temp=temp.next
        #         if (len(arr)<r and len_lnkd>k) and temp:
        #             temp1.next=ListNode(temp.val)
        #             temp1=temp1.next
        #             temp=temp.next
        #     else:
        #         head1=None
        #     arr.append(head1)
        # return arr

        