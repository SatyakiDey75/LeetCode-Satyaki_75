class Solution(object):
    def getMinDistance(self, nums, target, start):
        x=[]
        for i in range(len(nums)):
            if nums[i]==target:
                x.append(abs(i-start))
        return min(x)
        