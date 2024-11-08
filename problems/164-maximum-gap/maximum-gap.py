class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2:
            return 0
        if l == 2:
            return abs(nums[1] - nums[0])
        nums.sort()
        i, j = 0, 1
        diff = 0
        while i < l - 1:
            if nums[j] - nums[i] > diff:
                diff = nums[j] - nums[i]
            i += 1
            j += 1
        return diff