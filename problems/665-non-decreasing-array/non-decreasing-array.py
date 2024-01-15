class Solution(object):
    def checkPossibility(self, nums):
        j=None
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if j is not None:
                    return False
                j=i
        return j is None or j==0 or j==len(nums)-2 or nums[j-1]<=nums[j+1] or nums[j]<=nums[j+2]
            