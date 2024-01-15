class Solution(object):
    def singleNumber(self, nums):
        return [i for i in nums if nums.count(i)==1]
        