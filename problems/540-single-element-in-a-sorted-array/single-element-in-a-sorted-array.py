class Solution(object):
    def singleNonDuplicate(self, nums):
        n=len(nums)
        l=0
        r=n-1
        while(l<r):
            m=(l+r)//2
            if (m+1)%2:
                if nums[m+1]==nums[m]:
                    l=m+2
                else:
                    r=m
            else:
                if nums[m-1]==nums[m]:
                    l=m+1
                else:
                    r=m-1
        return nums[r]