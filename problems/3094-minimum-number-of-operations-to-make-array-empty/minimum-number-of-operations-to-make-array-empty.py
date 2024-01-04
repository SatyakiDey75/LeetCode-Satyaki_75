class Solution(object):
    def minOperations(self, nums):
        count=collections.Counter(nums)
        if 1 in count.values():
            return -1
        return sum((i+2)//3 for i in count.values())