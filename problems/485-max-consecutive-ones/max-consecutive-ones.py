class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c,r=0,0
        for i in nums:
            if i==1:
                c+=1
            else:
                r=max(r,c)
                c=0
        return max(r,c)