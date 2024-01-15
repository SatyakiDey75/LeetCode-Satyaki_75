class Solution(object):
    def maximumCount(self, nums):
        return max(sum(1 for i in nums if i>0),sum(1 for i in nums if i<0))
        