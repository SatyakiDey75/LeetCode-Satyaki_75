class Solution(object):
    def pivotIndex(self, nums):
        ls,s=0,sum(nums)
        for i,val in enumerate(nums):
            if ls==s-ls-val:
                return i
            ls+=val
        return -1

        # for i in range (len(nums)):
        #     if sum(nums[0:i])==sum(nums[i+1:]):
        #         return i
        # return -1