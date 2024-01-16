class Solution(object):
    def differenceOfSums(self, n, m):
        return sum(i for i in range(1,n+1) if i%m!=0)-sum(i for i in range(1,n+1) if i%m==0)
        