class Solution(object):
    def hIndex(self, citations):
        c = sorted(citations)[::-1]
        r = 0
        for i in range(len(c)):
            if c[i] >= i + 1:
                r = i + 1
            else:
                break
        return r
        