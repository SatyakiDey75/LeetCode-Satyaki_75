class Solution(object):
    def findDiagonalOrder(self, mat):
        m,n=len(mat),len(mat[0])
        l=[]
        k,j,i=1,0,0
        for _ in range (m*n):
            l.append(mat[i][j])
            i-=k
            j+=k
            if i==m:
                i=m-1
                j+=2
                k*=-1
            if j==n:
                j=n-1
                i+=2
                k*=-1
            if j<0:
                j=0
                k*=-1
            if i<0:
                i=0
                k*=-1
        return l