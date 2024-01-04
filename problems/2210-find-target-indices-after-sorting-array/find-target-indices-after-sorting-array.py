class Solution(object):
    def targetIndices(self, n, t):
        n.sort()
        l=[]
        for i in range (len(n)):
            if n[i]==t:
                l.append(i)
        return l
        