class Solution(object):
    def sortColors(self, nums):
        z,o,t=-1,-1,-1
        for i in nums:
            if i==0:
                t+=1
                o+=1
                z+=1
                nums[t]=2
                nums[o]=1
                nums[z]=0
            elif i==1:
                t+=1
                o+=1
                nums[t]=2
                nums[o]=1
            else:
                t+=1
                nums[t]=2