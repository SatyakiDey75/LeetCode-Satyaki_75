class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            nums[i]=s
        return nums