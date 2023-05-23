class Solution(object):
    def searchMatrix(self, matrix, target):
        f=0
        for i in range (0,len(matrix)):
            if target<matrix[i][len(matrix[i])-1]:
                j=0
                while (j<len(matrix[i])-1):
                    if matrix[i][j]==target:
                        f=1
                        return True
                    else:
                        j+=1
            elif target==matrix[i][len(matrix[i])-1]:
                f=1
                return True
            else:
                continue
        if f==0:
            return False
            