# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        temp, leng = head, 0
        while temp:
            leng += 1
            temp = temp.next
        count = 0
        temp = head
        while count < leng // 2 - 1:
            temp = temp.next
            count += 1
        toRev = temp.next
        rev2 = reverse(toRev)
        temp.next = rev2
        slow = head.next
        fast = rev2.next
        max_s = head.val + rev2.val
        for i in range (count):
            if max_s < (slow.val + fast.val):
                max_s = slow.val + fast.val
            slow = slow.next
            fast = fast.next

        return max_s
        