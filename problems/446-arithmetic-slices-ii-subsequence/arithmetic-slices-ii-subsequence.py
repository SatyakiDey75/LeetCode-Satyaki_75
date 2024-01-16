class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        r,dp=0,[defaultdict(int) for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                di=nums[i]-nums[j]
                
                dp[i][di]+=1
                if di in dp[j]:
                    dp[i][di]+=dp[j][di]
                    r+=dp[j][di]
        return r
        