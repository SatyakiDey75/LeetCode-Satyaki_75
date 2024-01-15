class Solution(object):
    def missingNumber(self, nums):
        l=[i for i in range(0,len(nums)+1)]
        return [i for i in l if i not in nums][0]
        