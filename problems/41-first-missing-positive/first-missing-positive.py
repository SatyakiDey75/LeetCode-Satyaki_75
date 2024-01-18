class Solution(object):
    def firstMissingPositive(self, nums):
        n=len(nums)
        for i in range(n):
            while nums[i]>0 and nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        for i,j in enumerate(nums):
            if j!=i+1:
                return i+1
        return n+1