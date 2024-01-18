# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        r,p=[],head
        while p!=None:
            r.append(p.val)
            p=p.next
        return r==r[::-1]