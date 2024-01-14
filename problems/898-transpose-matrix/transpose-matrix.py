import numpy
class Solution(object):
    def transpose(self, m):
        row = len(m)
        col = len(m[0])
        res = []
        for i in range(col):
            temp = []
            for j in range(row):
                temp.append(m[j][i])
            res.append(temp)
        return res
        