class Solution(object):
    def findWinners(self, matches):
        ans=[[] for i in range(2)]
        lc=collections.Counter()
        for i,j in matches:
            if i not in lc:
                lc[i]=0
            lc[j]+=1
        for p,n in lc.items():
            if n<2:
                ans[n].append(p)
        return [sorted(ans[0]),sorted(ans[1])]