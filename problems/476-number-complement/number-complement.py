class Solution(object):
    def findComplement(self, n):
        return int((bin(n)[2:].replace('0','2').replace('1','3').replace('3','0').replace('2','1')), 2)
        