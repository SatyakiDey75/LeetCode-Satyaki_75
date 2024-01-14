class Solution(object):
    def singleNumber(self, nums):
        ones,twos=0,0
        for num in nums:
            ones^=num&~twos
            twos^=num&~ones 
        return ones
        