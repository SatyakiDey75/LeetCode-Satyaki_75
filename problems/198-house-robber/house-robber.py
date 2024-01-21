class Solution(object):
    def rob(self, nums):
        p,q=0,0
        for num in nums:
            temp=max(p,q+num)
            q=p
            p=temp
        return p
            