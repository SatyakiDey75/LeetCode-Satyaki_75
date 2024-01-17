class Solution(object):
    def arrayRankTransform(self, arr):
        l1=[]
        l=sorted(set(arr))
        d={j:i+1 for i,j in enumerate(l)}
        for i in arr:
            l1.append(d[i])
        return l1