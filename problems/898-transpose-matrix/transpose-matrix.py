import numpy
class Solution(object):
    def transpose(self, m):
        c=len(m[0])
        r=len(m)
        tr=[]
        for i in range (c):
            l=[]
            for j in range (r):
                l.append(m[j][i])
            tr.append(l)
        return tr
        