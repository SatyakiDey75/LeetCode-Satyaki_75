class Solution(object):
    def sumBase(self, n, k):
        r=0
        while n>0:
            r+=n%k
            n//=k
        return r
        