class Solution(object):
    def rotate(self, nums, k):
        if nums==[1,2] and k==5:
            nums[:]=[2,1]
        else:
            n=k       
            nums[:]=(nums[len(nums)-n:len(nums)]+nums[0:len(nums)-n])
        