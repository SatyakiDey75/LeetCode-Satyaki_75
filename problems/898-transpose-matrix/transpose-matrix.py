import numpy
class Solution(object):
    def transpose(self, matrix):
        c=len(matrix[0])
        r=len(matrix)
        tr=[]
        for i in range (c):
            l=[]
            for j in range (r):
                l.append(matrix[j][i])
            tr.append(l)
        return tr
        