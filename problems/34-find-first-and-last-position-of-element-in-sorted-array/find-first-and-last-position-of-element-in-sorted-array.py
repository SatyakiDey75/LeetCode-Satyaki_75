class Solution(object):
    def searchRange(self, nums, target):
        l=[]
        for i in range (len(nums)):
            if nums[i]==target:
                l.append(i)
        if l==[]:
            return [-1,-1]
        return l*2 if len(l)==1 else l[::len(l)-1]