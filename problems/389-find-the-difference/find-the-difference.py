class Solution(object):
    def findTheDifference(self, s, t):
        c=collections.Counter(s)
        for i in t:
            if c[i]==0:
                return i
            c[i]-=1