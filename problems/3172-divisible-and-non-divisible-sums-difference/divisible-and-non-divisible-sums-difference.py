class Solution(object):
    def differenceOfSums(self, n, m):
        f,t=0,0
        for i in range (1,n+1):
            f,t=(f+i,t) if i%m!=0 else (f,t+i)
        return f-t
        