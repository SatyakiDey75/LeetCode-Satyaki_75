class Solution(object):
    def areOccurrencesEqual(self, s):
        l=[]
        for i in set(s):
            l.append(s.count(i))
        return l.count(l[0])==len(l)