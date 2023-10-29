class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix[0])
        d=0
        for i in range (0,n):
            c=n-1
            l=[]
            for j in range (0,n):
                l.append(matrix[c][d])
                c-=1
            matrix.append(l)
            d+=1
        for i in range ((len(matrix)//2)-1,-1,-1):
            matrix.pop(i)