class Solution(object):
    def shuffle(self, nums, n):
        r=[]
        for i,j in zip(nums[:n],nums[n:]):
            r.append(i)
            r.append(j)
        return r
        