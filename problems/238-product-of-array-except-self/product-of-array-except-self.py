class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if nums.count(0) > 1:
        #     return [0 for i in nums]
        # s = 1
        # for i in nums:
        #     if i != 0:
        #         s *= i
        
        # ans = []
        # if 0 in nums:
        #     for i in nums:
        #         if i != 0:
        #             ans.append(0)
        #         else:
        #             ans.append(s)
        #     return ans
        # for i in nums:
        #     if i != 0:
        #         ans.append(s // i)
        #     else:
        #         ans.append(s)
        # return ans

        ans = [1] * len(nums)
        
        l = 1
        for i in range(len(nums)):
            ans[i] *= l
            l *= nums[i]
        
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= r
            r *= nums[i]
    
        return ans  