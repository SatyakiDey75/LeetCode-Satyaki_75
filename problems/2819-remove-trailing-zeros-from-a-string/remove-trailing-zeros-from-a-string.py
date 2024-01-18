class Solution(object):
    def removeTrailingZeros(self, s):
        while s[-1]=='0':
            s=s[:-1]
        return s