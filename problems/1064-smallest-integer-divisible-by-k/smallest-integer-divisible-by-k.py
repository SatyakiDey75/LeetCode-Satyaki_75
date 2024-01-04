class Solution(object):
    def smallestRepunitDivByK(self, k):
        r=0
        for l in range (1,k+1):
            r=(r*10+1)%k
            if r==0:
                return l
        return -1
        