class Solution(object):
    def evenOddBit(self, n):
        r=[0]*2
        i=0
        while n>0:
            r[i]+=n&1
            n>>=1
            i^=1
        return r
            