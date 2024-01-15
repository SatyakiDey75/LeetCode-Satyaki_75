class Solution(object):
    def findNumbers(self, nums):
        return sum(1 for i in nums if len(str(i))%2==0)