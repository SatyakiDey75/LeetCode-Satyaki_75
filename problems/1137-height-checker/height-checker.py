class Solution(object):
    def heightChecker(self, heights):
        s=sorted(heights)
        return sum(s[i]!=heights[i] for i in range (len(s)))
        