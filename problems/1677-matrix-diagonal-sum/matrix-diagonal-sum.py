class Solution(object):
    def diagonalSum(self, mat):
        s=0
        for i in range (len(mat)):
            for j in range (len(mat)):
                if i==j or i+j==len(mat)-1:
                    s+=mat[i][j]
        return s
        