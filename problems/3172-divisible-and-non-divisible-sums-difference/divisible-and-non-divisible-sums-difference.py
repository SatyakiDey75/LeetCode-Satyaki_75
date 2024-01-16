class Solution(object):
    def differenceOfSums(self, n, m):
        f,t=0,0
        for i in range (1,n+1):
            if i%m!=0:
                f+=i
            else:
                t+=i
        return f-t
        