class Solution(object):
    def maxProduct(self, nums):
        res,dp_min,dp_max=nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            j=nums[i]
            pmax=dp_min
            pmin=dp_max
            if j<0:
                dp_min=min(pmin*j,j)
                dp_max=max(pmax*j,j)
            else:
                dp_min=min(pmax*j,j)
                dp_max=max(pmin*j,j)
            res=max(res,dp_max)
        return res
        