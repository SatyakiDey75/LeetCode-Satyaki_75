class Solution(object):
    def numberGame(self, nums):
        l=[]
        while len(nums)>0:
            a=nums.pop(nums.index(min(nums)))
            b=nums.pop(nums.index(min(nums)))
            l.append(b)
            l.append(a)
        return l