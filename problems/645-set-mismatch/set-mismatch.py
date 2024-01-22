class Solution(object):
    def findErrorNums(self, nums):
        for i in nums:
            if nums[abs(i)-1]<0:
                d=abs(i)
            else:
                nums[abs(i)-1]*=-1
        for i, j in enumerate(nums):
            if j>0:
                return [d,i+1]
        