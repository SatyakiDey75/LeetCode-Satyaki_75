class Solution(object):
    def numberGame(self, nums):
        l=[]
        nums.sort()
        for i in range (1,len(nums),2):
            l.append(nums[i])
            l.append(nums[i-1])
        return l