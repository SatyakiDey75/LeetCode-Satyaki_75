class Solution(object):
    def isGood(self, nums):
        n=len(nums)
        if n==0 or n==1:
            return False
        nums.sort()
        if nums[n-2]!=nums[n-1]:
            return False
        for i in range(n-1):
            if nums[i]!=i+1:
                return False
        return True