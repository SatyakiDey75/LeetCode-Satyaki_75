class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        l = sorted(score, reverse=True)
        ans = []
        for i in score:
            if l.index(i) == 0:
                ans.append("Gold Medal")
            elif l.index(i) == 1:
                ans.append("Silver Medal")
            elif l.index(i) == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(l.index(i) + 1))
        return ans