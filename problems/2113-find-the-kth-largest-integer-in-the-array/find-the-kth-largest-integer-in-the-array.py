class Solution(object):
    def kthLargestNumber(self, nums, k):
        l=[int(i) for i in nums]
        l.sort()
        return str(l[len(l)-k])