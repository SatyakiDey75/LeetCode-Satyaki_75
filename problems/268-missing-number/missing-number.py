class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        max_sum=(n*(n+1))/2
        return max_sum-sum(nums)