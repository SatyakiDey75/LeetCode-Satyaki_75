class Solution(object):
    def majorityElement(self, nums):
        b=None
        c=0
        for i in nums:
            if c==0:
                b=i
            c+=(1 if i==b else -1)
        return b 
        