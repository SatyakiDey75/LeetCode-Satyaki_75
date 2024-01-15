class Solution(object):
    def minSteps(self, s, t):
        count=collections.Counter(s)
        count.subtract(collections.Counter(t))
        return sum(abs(i) for i in count.values())//2