class Solution:
    def sumBase(self, n: int, k: int) -> int:
        r=0
        while n>0:
            if n//k:
                r+=n%k
                n//=k
            else:
                r+=n
                n=0
        return r