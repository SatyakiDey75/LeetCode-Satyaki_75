class Solution(object):
    def findMaxK(self, nums):
        nums.sort()
        i=0
        while i<len(nums) and nums[i]<0:
            if -nums[i] in nums:
                return -nums[i]
            i+=1
        return -1
