class Solution(object):
    def getNoZeroIntegers(self, n):
        d=1
        while '0' in str(n-d) or '0' in str(d):
            d+=1
        return [d,n-d]