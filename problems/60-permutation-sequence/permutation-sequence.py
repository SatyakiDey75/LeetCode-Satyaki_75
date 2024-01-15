class Solution(object):
    def getPermutation(self, n, k):
        l=[i for i in range (1,n+1)]
        r=list(itertools.permutations(l))[k-1]
        s=""
        for i in r:
            s+=str(i)
        return s