class Solution(object):
    def findDuplicates(self, nums):
        l=[]
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1] and nums[i] not in l:
                l.append(nums[i])
        return l