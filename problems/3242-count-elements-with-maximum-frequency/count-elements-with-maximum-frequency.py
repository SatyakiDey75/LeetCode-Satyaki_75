class Solution(object):
    def maxFrequencyElements(self, nums):
        l=[nums.count(i) for i in nums]
        return l.count(max(l))
        