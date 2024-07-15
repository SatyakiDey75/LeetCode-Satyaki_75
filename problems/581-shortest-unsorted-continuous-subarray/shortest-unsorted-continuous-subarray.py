class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l=sorted(nums)
        c,d=0,len(nums)
        for i in range(0,len(nums)):
            if l[i]!=nums[i]:
                break
            c+=1
        if c==len(nums):
            return 0
        for i in range(len(nums)-1,0,-1):
            if l[i]!=nums[i]:
                break
            d-=1

        return d-c