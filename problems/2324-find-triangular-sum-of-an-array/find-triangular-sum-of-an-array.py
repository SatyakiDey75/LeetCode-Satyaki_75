class Solution(object):
    def triangularSum(self, nums):
        l1=nums
        while len(l1)>1:
            l1=[(l1[i]+l1[i+1])%10 for i in range(0,len(l1)-1)]
        return l1[0]