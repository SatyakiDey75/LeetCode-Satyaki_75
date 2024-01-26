class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])
        # s=0
        # for i in range (0,len(nums),2):
        #     s+=nums[i]
        # return s
        