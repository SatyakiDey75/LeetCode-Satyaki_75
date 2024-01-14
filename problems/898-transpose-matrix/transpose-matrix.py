import numpy
class Solution(object):
    def transpose(self, m):
        tr=[]
        for i in range (len(m[0])):
            l=[]
            for j in range (len(m)):
                l.append(m[j][i])
            tr.append(l)
        return tr
        